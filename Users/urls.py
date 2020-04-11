from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),

    # Login Department
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
]
