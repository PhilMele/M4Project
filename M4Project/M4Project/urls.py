from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Allauth package
    path('accounts/', include('allauth.urls')),
]
