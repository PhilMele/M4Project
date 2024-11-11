from django.urls import path
from . import views

urlpatterns = [
    path('parking_manager_dashboard/', views.parking_manager_dashboard, name='parking-manager-dashboard'),
    path('parking_info/<int:parking_id>/', views.parking_info, name='parking-info'),
    path('parking_inspector/<int:parking_id>/', views.parking_inspector, name='parking-inspector'),
    # parking objects
    path('create_parking', views.create_parking, name='create-parking'),
    path('edit_parking/<int:parking_id>/', views.edit_parking, name='edit-parking'),
    path('delete_parking/<int:parking_id>/', views.delete_parking, name='delete-parking'),
    # rate objects
    path('add_rate/<int:parking_id>/', views.add_rate, name='add-rate'),
    path('edit_rate/<int:rate_id>/<int:parking_id>/', views.edit_rate, name='edit-rate'),
    path('delete_rate/<int:rate_id>/<int:parking_id>/', views.delete_rate, name='delete-rate'),


]