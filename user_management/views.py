from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from parking_activity.models import (
                                    Stay,
                                    EnterParking,
                                    LeaveParking,
                                    UserProfile
                                    )
from parking_management.models import Parking
from .forms import UserProfileForm
from django.contrib import messages

from django.contrib.auth.models import User


# error handlin imports
from django.http import HttpRequest
from django.core.exceptions import PermissionDenied
from django.core.exceptions import SuspiciousOperation

# allauth views
from allauth.account.views import SignupView


# Create your views here.
def is_parking_customer(request):
    if request.user.userprofile.user_type != 1:
        return False
    return True


class CustomSignupView(SignupView):
    def form_valid(self, form):
        # Save the user
        user = form.save()

        # Authenticate the user for login
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        if user is not None:
            login(self.request, user)
            return redirect('home')
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def index(request):
    # if user is parking_manager,
    # redirect to parking manager dashboard
    if not is_parking_customer(request):
        return redirect('parking-manager-dashboard')

    # look up if user has already an existing Stay object
    # and exclude objects that is matched with a LeaveParking object
    existing_stay_obj = Stay.objects.filter(
        user=request.user.userprofile
        ).exclude(
        id__in=LeaveParking.objects.values_list('stay_id', flat=True)
    )

    # declare variables as None so they are available in the
    # context even when `existing_stay_obj` does not exist
    parking_name = None
    stay_id = None
    lat = None
    long = None

    if existing_stay_obj.exists():
        for stay in existing_stay_obj:
            parking_name = stay.parking_name.name
            lat = stay.parking_name.latitude
            long = stay.parking_name.longitude
            stay_id = stay.id

    # checks if user has provided car registration
    car_reg = False
    if request.user.userprofile.car_registration:
        car_reg = True

    return render(
        request,
        'home/index.html', {
            'existing_stay_obj': existing_stay_obj,
            'parking_name': parking_name,
            'stay_id': stay_id,
            'lat': lat,
            'long': long,
            'car_reg': car_reg}
            )


@login_required
def user_account(request):
    user_profile = get_object_or_404(
        UserProfile,
        id=request.user.userprofile.id
        )

    return render(request, 'account/user_account.html', {
        'user_profile': user_profile})


@login_required
def edit_user_account(request):
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user)

    # check if user is already checked-in
    # look up if user has already an existing Stay object
    # and exclude objects that is matched with a LeaveParking object
    existing_stay_obj = Stay.objects.filter(
            user=request.user.userprofile
        ).exclude(
        id__in=LeaveParking.objects.values_list('stay_id', flat=True)
    )

    if existing_stay_obj:
        messages.error(
            request, "Your cannot your user profile whilst checked-in.")
        return redirect('user-account')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "User details updated.")
            return redirect('user-account')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'account/edit_user_account.html', {'form': form})


def is_parking_manager(request):

    if request.user.userprofile.user_type != 2:
        return False
    return True


def has_checked_in_users(request):

    if is_parking_manager(request):
        # list all parkings under management
        parking_portfolio = Parking.objects.filter(
                user=request.user.userprofile
                )

        for parking in parking_portfolio:
            stay_objects_count = Stay.objects.filter(
                parking_name=parking,
                paid=False
            ).count()
            if stay_objects_count > 0:
                return True


@login_required
def delete_user_account(request):

    # if is parking user
    if not is_parking_manager(request):
        # check if user is already checked-in
        # look up if user has already an existing Stay object
        # and exclude objects that is matched with a LeaveParking object
        existing_stay_obj = Stay.objects.filter(
            user=request.user.userprofile
            ).exclude(
            id__in=LeaveParking.objects.values_list('stay_id', flat=True)
        )
        if existing_stay_obj:
            messages.error(
                request,
                "Your delete your account whilst checked-in.")

            return redirect('user-account')

    # if is parking manager
    # prevent account deletion if cars are checked-in
    else:
        has_user = has_checked_in_users(request)
        if has_checked_in_users(request):
            messages.error(
                request,
                "You cannot delete your account while users are checked in.")
            return redirect('user-account')

    if request.method == 'POST':
        user = get_object_or_404(User, id=request.user.id)
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('home')
    return HttpResponseBadRequest("Invalid request method.")


# Error Handling

def handler404(request, exception):
    """ Handle 404 errors and render the custom 404 error page """
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """ Handle 500 errors and render the custom 500 error page """
    return render(request, 'errors/500.html', status=500)


def handler403(request, exception):
    """ Handle 403 errors and render the custom 403 error page """
    return render(request, 'errors/403.html', status=403)


def handler400(request, exception):
    """ Handle 400 errors and render the custom 400 error page """
    return render(request, 'errors/400.html', status=400)


def test_500_error(request: HttpRequest):
    """ Raise a test exception for the 500 error handler """
    raise Exception("Test 500 error")


def test_403_error(request):
    """ Raise a test exception for the 403 error handler """
    raise PermissionDenied("Test 403 error")


def test_400_error(request):
    """ Raise a test exception for the 400 error handler """
    raise SuspiciousOperation("Test 400 error")
