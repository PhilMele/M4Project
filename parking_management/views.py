from django.shortcuts import render
from user_management.models import UserProfile
from .models import Parking
# Create your views here.
def parking_manager_dashboard(request):
    
    all_parkings = Parking.objects.all()
    user_parking_list = Parking.objects.filter(user = request.user.userprofile)
    print(f"all_parkings = {all_parkings}")
    print(f"user_parking_list = {user_parking_list}")

    return render(request, 'dashboard/parking_manager_dashboard.html',{})