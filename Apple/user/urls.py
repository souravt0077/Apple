from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('Login/',views.user_login,name='login'),
    path('Register/',views.user_register,name='register'),
    path('Logout/',views.user_logout,name='logout'),
]
