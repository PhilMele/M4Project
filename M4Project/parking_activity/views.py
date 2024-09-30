from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StayForm
from .models import Stay, Fee, EnterParking, LeaveParking
from parking_management.models import Rate
from datetime import timedelta

# Create your views here.
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
        total_stay_time_hours = total_stay_time.total_seconds() / 3600
        print(f'total_stay_time in hours = {total_stay_time_hours}')
    

        #look for applicate rate for parking ID and total stay again rate.hour_range
        rate_available = Rate.objects.filter(parking_name=stay.parking_name).order_by('hour_range')
        
        for rate in rate_available:
            print(f'rate_available = Hour range:{rate.hour_range}; Rate:{rate.rate}')
        #return applicable fee
        #apply applicable fee against total user stay


        return redirect('home')  
    except Stay.DoesNotExist:
        messages.error(request, "Stay does not exist.")
        return redirect('home') 

@login_required
def history(request):
    user_history = Stay.objects.filter(user=request.user.userprofile).order_by('-id')
    print(user_history)

    #create empty list of enter and leave parking
    enter_parking_history = []
    leave_parking_history = []
    Fee = None

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