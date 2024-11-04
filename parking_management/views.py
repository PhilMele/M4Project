from django.shortcuts import render
from user_management.models import UserProfile
from .models import Parking
# Create your views here.
def parking_manager_dashboard(request):
    user_parking_list = Parking.objects.filter(user = request.user.userprofile)
    print(f"user_parking_list = {user_parking_list}")
    return render(request, 'dashboard/parking_manager_dashboard.html',{
        'user_parking_list':user_parking_list,
    })

def parking_info(request, parking_id):
    print(f"parking_info()")
    return render(request, 'parking_info/parking_info.html',{})