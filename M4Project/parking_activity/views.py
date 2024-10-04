from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StayForm
from .models import Stay, EnterParking, LeaveParking, UserPayment
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from parking_management.models import Rate
from datetime import timedelta
from decimal import Decimal
import math

#stripe modul imports

from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
import time


# Create your views here.
# Mark user as entering parking
@login_required
def enter(request):
    if request.method == "POST":
        stayform = StayForm(request.POST)
        if stayform.is_valid():
            print("for is valid")
            staydata = stayform.save(commit=False)
            staydata.user = request.user.userprofile
            staydata.save()
            messages.success(request, "Stay data saved successfully.")
            enter_parking_obj = EnterParking.objects.create(
                user=request.user.userprofile,
                parking_name=staydata.parking_name,
                stay=staydata)
            return redirect('home')

        else:
            for error in list(stayform.errors.values()):
                messages.error(request, error)
    else:
        stayform = StayForm()

    return render(request, 'stays/enter.html', {'stayform': stayform})


# Mark user as leaving parking
@login_required
def leave(request, stay_id):
    # Retrieve the existing Stay object
    try:
        stay = Stay.objects.get(id=stay_id, user=request.user.userprofile)
        print(f'stay id = {stay}')
        # Create a LeaveParking entry
        leave_parking = LeaveParking.objects.create(
            user=request.user.userprofile,
            parking_name=stay.parking_name,
            stay=stay,
        )
        messages.success(request, "Successfully left the parking.")
        #calculte fee relating to stay
        #calculate total user stay

        #retrieve enter timestamp
        enter_time = EnterParking.objects.get(stay=stay_id)
        print(f'enter_time = {enter_time.timestamp_enter}')

        #retrieve leave timestamp
        exit_time = LeaveParking.objects.get(stay=stay_id)
        print(f'exit_time = {exit_time.timestamp_leave}')

        #difference between enter and leave time
        total_stay_time = exit_time.timestamp_leave - enter_time.timestamp_enter
        print(f'total_stay_time = {total_stay_time}')

        # Convert total_stay_time to hours
        total_stay_time_hours = Decimal(total_stay_time.total_seconds()) / Decimal(3600)
        print(f'total_stay_time in hours = {total_stay_time_hours}')

        applicable_fee = calculate_user_fee(stay, total_stay_time_hours)

        if applicable_fee:
            print(f'applicable_fee is {applicable_fee}')
            fee_form(request, applicable_fee, stay_id)
            payment(request,applicable_fee, stay_id)
        else:
            print(f'no applicable fee')

        return redirect('home')  
    except Stay.DoesNotExist:
        messages.error(request, "Stay does not exist.")
        return redirect('home') 


# Fee calculation logic
def calculate_user_fee(stay, total_stay_time_hours):
    #apply applicable fee against total user stay
    #round up stay to next hour value
    roundedup_total_stay_time_hours = math.ceil(total_stay_time_hours)
    print(f'rounded_total_stay_time_hours = {roundedup_total_stay_time_hours}')

    #look for applicate rate for parking ID and total stay again rate.hour_range
    rate_available = Rate.objects.filter(parking_name=stay.parking_name).order_by('hour_range')

    #return applicable fee
    #create variable to attach closest rate to it during loop
    closest_rate = None
    for rate in rate_available:
        print(f'rate_available = Hour range:{rate.hour_range}; Rate:{rate.rate}')
        if total_stay_time_hours <= Decimal(rate.hour_range):
            closest_rate = rate
            break 
    
    #if the user stayed longer than longest rate
    #apply the latest rate on the list
    if closest_rate is None and rate_available.exists():
        closest_rate = rate_available.last()

    if closest_rate:
        print(f'closest rate is {closest_rate}')
        applicable_fee = closest_rate.rate * roundedup_total_stay_time_hours
        print(f'applicable_fee = {applicable_fee}')
        return (applicable_fee)
    else:
        print('Looks like there is a problem!')
        return None


# Create new Fee model object agianst user name
@login_required     
def fee_form(request, applicable_fee,stay_id ):
    try:
        stay = Stay.objects.get(id=stay_id)
        stay.calculated_fee = applicable_fee
        stay.save()
        print(f"Stay object {stay_id} updated with calculated_fee: {stay.calculated_fee}")
    except Stay.DoesNotExist:
        print('Stay object does not exist')

@login_required 
def payment(request,applicable_fee, stay_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['cards'],
            line_items =[
                {
                    'price':applicable_fee,
                    'quantity':1,

                },
            ],
            mode = 'payment',
            customer_creation = 'always',
            succesful_url = settings.REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url = settings.REDIRECT_DOMAIN + '/payment_cancelled',
        )
        print(f'checkout_session = {checkout_session}')
        return redirect(checkout_session.url, code=303)

#stripe payment logic
@login_required
def payment_successful(request):
    stripe.api_key = stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    checkout_session_id = request.GET.get('session_id', None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)
    user_id = request.user.userprofile.id
    user_payment = UserPayment.objects.get(user=user_id)
    user_payment.stripe_checkout_id = checkout_session_id
    user_payment.save()
    return render(request, 'payment_successful.html',{'customer':customer})

@login_required
def payment_cancelled(request):
    return render(request, 'payment_cancelled.html')

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    time.sleep(10) # time left to stripe to process payment
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session.get('id', None)
        time.sleep(15)
        user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
        line_items = stripe.checkout.Session.list_line_items(session_id,limit=1)
        user_payment.payment.bool = True
        user_payment.save()
    return HttpResponse(status=200)



@login_required
def history(request):
    user_history = Stay.objects.filter(user=request.user.userprofile).order_by('-id')
    print(user_history)

    #create empty list of enter and leave parking
    enter_parking_history = []
    leave_parking_history = []


    for stay in user_history:
        #I need to return timestamp of child EnterParking
        #I filtjer all EnterParking objects with a matching stay ID
        enter_object = EnterParking.objects.filter(stay=stay)
        print(f'enter_object: {enter_object}')
        #append resuls to empty list created above
        for entry in enter_object:
            enter_parking_history.append({
                'stay': stay,
                'entry': entry
            })
        
        #I need to return timestamp of child LeaverParking
        leave_object = LeaveParking.objects.filter(stay=stay)
        print(f'leave_object: {leave_object}')
        #append resuls to empty list created above
        for leave in leave_object:
            leave_parking_history.append({
                'stay': stay,
                'leave': leave
            })

        
        
    return render(request, 'history/history.html', {
        'user_history':user_history,
        'enter_parking_history':enter_parking_history,
        'leave_parking_history':leave_parking_history,
        })