""" Defines URL patterns for account. """

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),

    # Registration page.
    path('register/',views.register, name='register'),
]