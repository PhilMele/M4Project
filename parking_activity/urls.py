from django.urls import path
from . import views

urlpatterns = [
    path('enter/', views.enter, name='enter'),
    path('enter/<int:parking_id>/', views.enter, name='enter_with_parking_id'),
    path('leave/<int:stay_id>/', views.leave, name='leave'),
    path('history/', views.history, name='history'),
    path('get-parking-location/', views.get_parking_location, name='get_parking_location'),
    path('get_parking_rates/<int:parking_id>/', views.get_parking_rates, name='get_parking_rates'),

    #payment paths
    path('payment_successful/', views.payment_successful, name='payment-successful'),
    path('payment_cancelled/',views.payment_cancelled, name='payment-cancelled'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook'),
]