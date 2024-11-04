from django.urls import path
from . import views

urlpatterns = [
    path('parking_manager_dashboard/', views.parking_manager_dashboard, name='parking-manager-dashboard'),
    path('parking_info/<int:parking_id>/', views.parking_info, name='parking-info'),

]