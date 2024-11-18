from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from parking_activity.models import Stay, EnterParking, LeaveParking



# Create your views here.
#register user
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def index(request):
    # look up if user has already an existing Stay object
    # and exclude objects that is matched with a LeaveParking object 
    existing_stay_obj = Stay.objects.filter(user=request.user.userprofile).exclude(
        id__in=LeaveParking.objects.values_list('stay_id', flat=True)
    )
    #declare variables as None so they are available in the 
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
    
    return render(request, 'home/index.html',{
        'existing_stay_obj':existing_stay_obj,
        'parking_name':parking_name,
        'stay_id':stay_id,
        'lat':lat,
        'long':long})

def user_account(request):
    return render(request, 'account/user_account.html', {})
