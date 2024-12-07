from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# allauth view paths
from .views import CustomSignupView

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='home'),
    path('user_account/', views.user_account, name='user-account'),
    path('edit_user_account/', views.edit_user_account, name='edit-user-account'),
    path('delete_user_account/', views.delete_user_account, name='delete-user-account'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),

    # Error hanlder testing
    path('test_500_error/', views.test_500_error, name='test-500-error'),
    path('test_403_error/', views.test_403_error, name='test-403-error'),
    path('test_400_error/', views.test_400_error, name='test-400-error'),

]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)