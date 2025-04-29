
from django.urls import path
from SkinVisionApp import views
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from .views import save_annotation, upload_image_view, delete_image
from . import views
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('', RedirectView.as_view(pattern_name='dashboard'), name='home'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('annotate/', views.annotation_view, name='annotate'),
    path('api/save_annotation/', save_annotation, name='save_annotation'),
    path('registered_users/', views.registered_users_view, name='registered_users'),
    path('upload_image/', views.upload_image_view, name='upload_image'),
    path('delete_image/<int:image_id>/', delete_image, name='delete_image'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)