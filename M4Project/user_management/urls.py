from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='home')
]
