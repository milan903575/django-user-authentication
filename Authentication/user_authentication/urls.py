from django.urls import path
from .views import (
    signup_view, login_view, logout_view, dashboard_view, 
    profile_view, change_password_view, forgot_password_view, reset_password_view
)

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('reset-password/<uidb64>/<token>/', reset_password_view, name='reset_password'),
    path('change-password/', change_password_view, name='change_password'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
]
