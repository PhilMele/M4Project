from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StayForm
from .models import Stay, EnterParking, LeaveParking
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from parking_management.models import Rate, Parking
from datetime import timedelta
from decimal import Decimal
import math
from django.core.exceptions import ValidationError
# stripe modul imports

from django.conf import settings
import stripe
import time
from django.http import JsonResponse

# geolocation module
from geopy import distance

# email sending
from django.core.mail import send_mail
from django.template.loader import render_to_string

# debugging
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def is_parking_customer(request):
    if request.user.userprofile.user_type != 1:
        return False
    return True


@login_required
def get_parking_location(request):
    # checks if user has provided car registration
    # in their userprofile
    if not request.user.userprofile.car_registration:
        messages.error(
            request,
            "You need to provide your car registration before checking in. "
            "Connect to your profile to add it."
        )
        return redirect('home')

    # if no active parking, user is redirected to home page
    is_parking = Parking.objects.filter(active=True)
    if not is_parking:
        messages.error(request, "There is no parking available yet.")
        return redirect('home')

    if request.method == "POST":

        # capture user current location
        user_latitude = request.POST.get('latitude')
        user_longitude = request.POST.get('longitude')

        if user_latitude and user_longitude:
            user_location_tuple = (float(user_latitude), float(user_longitude))

            # match current user location to parking radius (if any)
            parkings = Parking.objects.filter(active=True)

            # create for loop of parkings
            for parking in parkings:

                parking_radius = float(parking.radius)

                # set parking location in tuple
                parking_location_tuple = (
                    float(parking.latitude),
                    float(parking.longitude)
                )

                # measure distance between user location and parking location
                locations_distance = distance.distance(
                    user_location_tuple,
                    parking_location_tuple).meters

                if locations_distance <= parking_radius:
                    parking_name = parking

                    # return redirect to enter page with parking ID
                    return redirect(
                        'enter_with_parking_id',
                        parking_id=parking_name.id)

            messages.error(
                request,
                "We could not locate you. Please select parking."
                )

            return redirect('enter')

    return redirect('home')


# used to get parking rates through API (dynamically generated with js)
# note: safe = False allows to return a list instead of a dictonnary
def get_parking_rates(request, parking_id):
    rates = Rate.objects.filter(parking_name_id=parking_id).values(
        'rate_name',
        'hour_range',
        'rate',
    )
    return JsonResponse(list(rates), safe=False)


# Mark user as entering parking
@login_required
def enter(request, parking_id=None):
    # if user is parking_manager,
    # redirect to parking manager dashboard
    if not is_parking_customer(request):
        return redirect('parking-manager-dashboard')

    parking_name = None
    parking_list = Parking.objects.filter(active=True)

    if parking_id:
        parking_name = get_object_or_404(Parking, id=parking_id)

        # if parking id is not null
        if request.method == "POST":
            stayform = StayForm(request.POST)
            if stayform.is_valid():
                staydata = stayform.save(commit=False)
                staydata.user = request.user.userprofile
                staydata.parking_name = parking_name  # attach it to parking_id
                staydata.save()
                messages.success(
                    request,
                    f"You have successfully checked-in at {parking_name}")

                enter_parking_obj = EnterParking.objects.create(
                    user=request.user.userprofile,
                    parking_name=parking_name,
                    stay=staydata
                    )
                return redirect('home')
            else:
                for error in list(stayform.errors.values()):
                    messages.error(request, error)

        # if null
        else:
            stayform = StayForm()

    else:
        if request.method == "POST":

            # get the parking_name value from POST
            parking_id = request.POST.get('parking_name')
            if parking_id:
                parking_name = get_object_or_404(Parking, id=parking_id)
            else:
                messages.error(
                        request,
                        "Please select a valid parking location.")
                return redirect('enter')

            stayform = StayForm(request.POST)
            if stayform.is_valid():
                staydata = stayform.save(commit=False)
                staydata.user = request.user.userprofile
                staydata.save()
                messages.success(
                    request,
                    f'You have successfully checked-in at {parking_name}'
                    )
                enter_parking_obj = EnterParking.objects.create(
                    user=request.user.userprofile,
                    parking_name=parking_name,
                    stay=staydata
                    )
                return redirect('home')
            else:
                for error in list(stayform.errors.values()):
                    messages.error(request, error)
        else:
            stayform = StayForm()

    return render(request, 'stays/enter.html', {
        'stayform': stayform,
        'parking_id': parking_id,
        'parking_list': parking_list,
        'parking_name': parking_name})


# Mark user as leaving parking
@login_required
def leave(request, stay_id):

    # if user is parking_manager,
    # redirect to parking manager dashboard
    if not is_parking_customer(request):
        return redirect('parking-manager-dashboard')

    # Retrieve the existing Stay object
    try:
        stay = Stay.objects.get(id=stay_id, user=request.user.userprofile)

        # Create a LeaveParking entry
        leave_parking = LeaveParking.objects.create(
            user=request.user.userprofile,
            parking_name=stay.parking_name,
            stay=stay,
        )

        # retrieve enter timestamp
        enter_time = EnterParking.objects.get(stay=stay_id)

        # retrieve leave timestamp
        exit_time = LeaveParking.objects.get(stay=stay_id)

        # difference between enter and leave time
        total_stay_time = (
            exit_time.timestamp_leave - enter_time.timestamp_enter
        )

        # Convert total_stay_time to hours
        total_stay_time_hours = (
            Decimal(total_stay_time.total_seconds()) / Decimal(3600))

        applicable_fee = calculate_user_fee(stay, total_stay_time_hours)

        if applicable_fee:
            fee_form(request, applicable_fee, stay_id)
            return payment(request, applicable_fee, stay_id)

        return redirect('home')

    except Stay.DoesNotExist:
        messages.error(request, "Stay does not exist.")
        return redirect('home')


# Fee calculation logic
def calculate_user_fee(stay, total_stay_time_hours):

    # apply applicable fee against total user stay
    # round up stay to next hour value
    roundedup_total_stay_time_hours = math.ceil(total_stay_time_hours)

    # look for applicate rate for parking ID
    # and total stay again rate.hour_range
    rate_available = (
        Rate.objects.filter(
            parking_name=stay.parking_name).order_by('hour_range'))

    # return applicable fee
    # create variable to attach closest rate to it during loop
    closest_rate = None

    for rate in rate_available:
        if total_stay_time_hours <= Decimal(rate.hour_range):
            closest_rate = rate
            break

    # if the user stayed longer than longest rate
    # apply the latest rate on the list
    if closest_rate is None and rate_available.exists():
        closest_rate = rate_available.last()

    if closest_rate:
        applicable_fee = closest_rate.rate * roundedup_total_stay_time_hours
        return (applicable_fee)
    else:
        return None


# add Fee value to stay_id
@login_required
def fee_form(request, applicable_fee, stay_id):
    try:
        stay = Stay.objects.get(id=stay_id)
        stay.calculated_fee = applicable_fee
        stay.save()
    except Stay.DoesNotExist:
        logger.error(f'Stay object with id {stay_id} does not exist.')


@login_required
def payment(request, applicable_fee, stay_id):
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
        amount_int = int(applicable_fee * 100)  # Convert to integer for Stripe

        # Check if user already has a stripe customer ID
        if not request.user.userprofile.stripe_customer_id:
            customer = stripe.Customer.create(
                email=request.user.email
            )
            request.user.userprofile.stripe_customer_id = customer.id
            request.user.userprofile.save()

        # Create a price object in Stripe
        price_object = stripe.Price.create(
            unit_amount=amount_int,
            currency="gbp",
            product_data={
                "name": "Parking Fee"
            }
        )

        # Create checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price_object.id,
                'quantity': 1,
            }],
            mode='payment',
            customer=request.user.userprofile.stripe_customer_id,
            success_url=(
                settings.REDIRECT_DOMAIN +
                'parking_activity/payment_successful?session_id=' +
                '{CHECKOUT_SESSION_ID}'
            ),
            cancel_url=settings.REDIRECT_DOMAIN +
            'parking_activity/payment_cancelled',
        )

        # Update the Stay model with the checkout session ID
        stay = Stay.objects.get(id=stay_id)
        stay.stripe_checkout_id = checkout_session.id
        stay.save()

        # Redirect to Stripe checkout page
        return redirect(checkout_session.url)

    except Exception as e:
        logger.error(f"Error occurred in payment processing: {str(e)}")
        return HttpResponse("Error occurred in payment processing")


# stripe payment logic
@login_required
def payment_successful(request):

    # if user is parking_manager,
    # redirect to parking manager dashboard
    if not is_parking_customer(request):
        return redirect('parking-manager-dashboard')

    stripe.api_key = stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    checkout_session_id = request.GET.get('session_id', None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)

    messages.success(request, "Payment successfull!")

    return render(
        request,
        'payment/payment_successful.html', {'customer': customer})


@login_required
def payment_cancelled(request):

    # if user is parking_manager,
    # redirect to parking manager dashboard
    if not is_parking_customer(request):
        return redirect('parking-manager-dashboard')

    return render(request, 'payment/payment_cancelled.html')


@csrf_exempt
def stripe_webhook(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

    payload = request.body
    signature_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    webhook_secret = settings.STRIPE_WEBHOOK_SECRET_TEST
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, webhook_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session.get('id', None)
        time.sleep(15)
        try:
            # retrieve user payment record
            stay = Stay.objects.get(stripe_checkout_id=session_id)
            line_items = (
                stripe.checkout.Session.list_line_items(
                    session_id, limit=1
                    )
                )
            stay.paid = True
            stay.save()

            subject = "[GeoPay] Payment Confirmation"
            context = {
                'username': stay.user.user.username,
                'stripe_checkout_id': stay.stripe_checkout_id,
                'transaction_id': stay.id,
                'amount_paid': stay.calculated_fee,
                'parking_name': stay.parking_name.name,
            }

            # prepare email
            message = render_to_string(
                'email/payment_confirmation_email.html',
                context)
            email_reciever = stay.user.user.email

            # send email
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email_reciever],
                    html_message=message,
                    fail_silently=False,
                )
                logger.info('Email sent successfully')
            except Exception as e:
                logger.error('Error sending email: %s', str(e))
        except Stay.DoesNotExist:
            logger.error(
                "Stay record not found for session ID: %s", session_id)
        except Exception as e:
            logger.error("Error handling webhook: %s", str(e))

    return HttpResponse(status=200)


@login_required
def history(request):

    # if user is parking_manager,
    # redirect to parking manager dashboard
    if not is_parking_customer(request):
        return redirect('parking-manager-dashboard')

    user_history = Stay.objects.filter(
        user=request.user.userprofile
        ).order_by('-id')

    # create empty list of enter and leave parking
    enter_parking_history = []
    leave_parking_history = []

    for stay in user_history:
        enter_object = EnterParking.objects.filter(stay=stay)
        # append resuls to empty list created above
        for entry in enter_object:
            enter_parking_history.append({
                'stay': stay,
                'entry': entry
            })

        leave_object = LeaveParking.objects.filter(stay=stay)

        # append resuls to empty list created above
        for leave in leave_object:
            leave_parking_history.append({
                'stay': stay,
                'leave': leave
            })

    return render(request, 'history/history.html', {
        'user_history': user_history,
        'enter_parking_history': enter_parking_history,
        'leave_parking_history': leave_parking_history,
        })
