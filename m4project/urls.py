from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Allauth package
    path('accounts/', include('allauth.urls')),
    path('', include('user_management.urls')),
    path('parking_activity/', include('parking_activity.urls')),
    path('parking_management/', include('parking_management.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
