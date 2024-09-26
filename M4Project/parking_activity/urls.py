from django.urls import path
from . import views

urlpatterns = [
    path('enter/', views.enter, name='enter')

]