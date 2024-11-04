from django.urls import path
from . import views

urlpatterns = [
    path('parking_manager_dashboard', views.parking_manager_dashboard, name='parking-manager-dashboard'),

]