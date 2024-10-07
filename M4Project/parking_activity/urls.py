from django.urls import path
from . import views

urlpatterns = [
    path('enter/', views.enter, name='enter'),
    path('leave/<int:stay_id>/', views.leave, name='leave'),
    path('history/', views.history, name='history'),

    #payment paths
    path('payment_successful/',views.payment_successful, name='payment-succesful'),
    path('payment_cancelled/',views.payment_cancelled, name='payment-cancelled'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook')



]