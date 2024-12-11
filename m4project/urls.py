from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, handler403, handler400

urlpatterns = [
    path('admin/', admin.site.urls),
    # Allauth package
    path('accounts/', include('allauth.urls')),
    path('', include('user_management.urls')),
    path('parking_activity/', include('parking_activity.urls')),
    path('parking_management/', include('parking_management.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'user_management.views.handler404'
handler500 = 'user_management.views.handler500'
handler403 = 'user_management.views.handler403'
handler400 = 'user_management.views.handler400'
