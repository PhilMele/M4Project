from django.shortcuts import render, redirect, get_object_or_404
from user_management.models import UserProfile
from parking_activity.models import Stay
from .models import Parking, Rate, IllegalParking
from .forms import ParkingForm, RateForm, IllegalParkingForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def parking_manager_dashboard(request):
    user_parking_list = Parking.objects.filter(user = request.user.userprofile)

    return render(request, 'dashboard/parking_manager_dashboard.html',{
        'user_parking_list':user_parking_list,
    })

def parking_inspector(request,parking_id):
    parking_users = Stay.objects.filter(
        parking_name=parking_id,
        paid = False,
        )
    illegal_users = IllegalParking.objects.filter(
        parking_name=parking_id,
    )

    parking = get_object_or_404(Parking, id = parking_id)
    
    # record list of cars illegally parked
    if request.method == "POST":
        illegalparkingform = IllegalParkingForm(request.POST)
        if illegalparkingform.is_valid():
            illegalparkingformdata = illegalparkingform.save(commit=False)
            illegalparkingformdata.inspector = request.user.userprofile
            illegalparkingformdata.parking_name = parking
            illegalparkingformdata.save()
            print(f'illegalparkingformdata.save = {illegalparkingformdata.save}')
            messages.success(request,"Illegal Registration saved.")
            return redirect('parking-inspector', parking_id=parking_id)
        else:
            messages.success(request,"Oops. Something did not work")
    else:
        illegalparkingform = IllegalParkingForm()
        # TODO : return list of all cars parked in parking ID + handle front end if None
        # TODO : create  form for inspector to enter list of cars parked illegally
        # TODO: make this list available in another page
        # TODO: Implement email system + forgot password
        # TODO: implement static stuff
        # TODO: Front end
    
    return render(request, 'parking_inspector/parking_inspector.html',{ 
        'parking_users':parking_users,
        'illegal_users':illegal_users,
        'illegalparkingform':illegalparkingform,
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
    stay_objects_count = parking_space_available(parking_id)
    parking = get_object_or_404(Parking, id=parking_id)
    rates = Rate.objects.filter(parking_name=parking)
    return render(request, 'parking_info/parking_info.html',{
        'parking':parking,
        'rates':rates,
        'stay_objects_count':stay_objects_count
    })

def parking_space_available(parking_id):
    # identify parking
    parking = get_object_or_404(Parking, id=parking_id)
    
    # count of stay objects with paid = false
    stay_objects_count = Stay.objects.filter(
        parking_name= parking,
        paid = False).count()
    
    return stay_objects_count

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