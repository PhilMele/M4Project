from django.shortcuts import render, redirect, get_object_or_404
from user_management.models import UserProfile
from .models import Parking, Rate
from .forms import ParkingForm, RateForm

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
# Parking objects
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
    return render(request, 'parking/create_parking/create_parking.html',{
        'parkingform':parkingform
    })

@login_required
def parking_info(request, parking_id):

    print({parking_id})
    parking = get_object_or_404(Parking, id=parking_id)
    rates = Rate.objects.filter(parking_name=parking)
    return render(request, 'parking_info/parking_info.html',{
        'parking':parking,
        'rates':rates,
    })

@login_required
def edit_parking(request, parking_id):

    parking = get_object_or_404(Parking, id=parking_id)
    
    if request.method == "POST":
        editparkingform = ParkingForm(request.POST, instance=parking)
       
        if editparkingform.is_valid():
            
            editparkingform.save()
            messages.success(request, "Parking details updated successfully.")
            return redirect('parking-info', parking_id=parking.id)
        else:
        
            messages.error(request, "There was an issue updating the parking details.")
    else:
        
        editparkingform = ParkingForm(instance=parking)

    return render(request, 'parking/edit_parking/edit_parking.html', {
        'editparkingform': editparkingform,
    })


@login_required
def delete_parking(request, parking_id):
    parking = get_object_or_404(Parking, id=parking_id, user=request.user.userprofile)
    parking.delete()
    messages.success(request, "Parking deleted.")
    return redirect('parking-manager-dashboard')

# Rate objects
@login_required
def add_rate(request, parking_id):
    parking = get_object_or_404(Parking, id=parking_id)
    if request.method == "POST":
        rateform = RateForm(request.POST)
        if rateform.is_valid():
            ratedata = rateform.save(commit = False)
            ratedata.user = request.user.userprofile
            ratedata.parking_name = parking
            ratedata.save()
            messages.success(request,"New rate created successfully.")
            return redirect('parking-info', parking_id=parking_id)
        else:
            messages.success(request,"Oops. Something did not work")
    else:
        rateform = RateForm()

    return render(request, 'rate/add_rate/add_rate.html', {
        'rateform':rateform,
        
    })


@login_required
def edit_rate(request, parking_id, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)
    parking = get_object_or_404(Parking, id=parking_id)
    parking_id = parking.id
    print(f'parking_id = {parking_id}')

    if request.method == "POST":
        editrateform = RateForm(request.POST, instance=rate) 
        if editrateform.is_valid():
            editrateform.save()
            messages.success(request, "Parking details updated successfully.")
            return redirect('parking-info', parking_id=parking_id)
        else:
        
            messages.error(request, "There was an issue updating the parking details.")
    else:
        
        editrateform = RateForm(instance=rate)

    return render(request, 'rate/edit_rate/edit_rate.html', {
        'editrateform': editrateform,
    })

@login_required
def delete_rate(request, parking_id, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)
    rate.delete()
    messages.success(request, "Rate deleted.")
    return redirect('parking-info', parking_id=parking_id)