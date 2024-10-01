from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from parking_activity.models import Stay, EnterParking, LeaveParking


# Create your views here.
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
    print(f'existing_stay_obj = {existing_stay_obj}')
    if existing_stay_obj.exists():
        for stay in existing_stay_obj:
            parking_name = stay.parking_name.name
            stay_id = stay.id
    
    return render(request, 'home/index.html',{
        'existing_stay_obj':existing_stay_obj,
        'parking_name':parking_name,
        'stay_id':stay_id})