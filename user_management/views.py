from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from parking_activity.models import (Stay,
                                    EnterParking,
                                    LeaveParking,
                                    UserProfile)
from .forms import UserProfileForm
from django.contrib import messages

# error handlin imports
from django.http import HttpRequest
from django.core.exceptions import PermissionDenied
from django.core.exceptions import SuspiciousOperation

# allauth views
from allauth.account.views import SignupView

# Create your views here.
def is_parking_customer(request):
    print(f'request.user.userprofile.user_type: {request.user.userprofile.user_type}')
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
    existing_stay_obj = Stay.objects.filter(user=request.user.userprofile).exclude(
        id__in=LeaveParking.objects.values_list('stay_id', flat=True)
    )

    # declare variables as None so they are available in the 
    # context even when `existing_stay_obj` does not exist
    parking_name = None
    stay_id = None
    lat = None
    long = None
    print(f'existing_stay_obj = {existing_stay_obj}')
    if existing_stay_obj.exists():
        for stay in existing_stay_obj:
            parking_name = stay.parking_name.name
            lat = stay.parking_name.latitude
            long = stay.parking_name.longitude
            stay_id = stay.id

    # checks if user has provided car registration
    car_reg = False
    if request.user.userprofile.car_registration:
        car_reg= True
    
    return render(request, 'home/index.html',{
        'existing_stay_obj':existing_stay_obj,
        'parking_name':parking_name,
        'stay_id':stay_id,
        'lat':lat,
        'long':long,
        'car_reg':car_reg})

def user_account(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():  
            form.save()
            messages.success(request, "User details updated.")
            return redirect('user-account')  
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'account/user_account.html', {'form': form})

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
