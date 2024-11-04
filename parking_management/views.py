from django.shortcuts import render, redirect
from user_management.models import UserProfile
from .models import Parking
from .forms import ParkingForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def parking_manager_dashboard(request):
    user_parking_list = Parking.objects.filter(user = request.user.userprofile)
    print(f"user_parking_list = {user_parking_list}")


    return render(request, 'dashboard/parking_manager_dashboard.html',{
        'user_parking_list':user_parking_list,
    })

@login_required
def create_parking(request):
    if request.method == "POST":
        parkingform = ParkingForm(request.POST)
        if parkingform.is_valid():
            parkingdata = parkingform.save(commit = False)
            parkingdata.user = request.user.userprofile
            parkingdata.save()
            new_parking = parkingform.save()
            new_parking_id = new_parking.id
            messages.success(request,"Parking data saved successfully.")
            return redirect('parking-info', parking_id=new_parking_id)
        else:
            messages.success(request,"Oops. Something did not work")
    else:
        parkingform = ParkingForm()
    return render(request, 'create_parking/create_parking.html',{
        'parkingform':parkingform
    })

@login_required
def parking_info(request, parking_id):
    print(f"parking_info()")
    return render(request, 'parking_info/parking_info.html',{})