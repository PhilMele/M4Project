from django.urls import path
from . import views

urlpatterns = [
    path('enter/', views.enter, name='enter'),
    path('leave/<int:stay_id>/', views.leave, name='leave'),
    path('history/', views.history, name='history')

]