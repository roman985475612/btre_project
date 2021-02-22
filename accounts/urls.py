from django.urls import path

from .apps import AccountsConfig
from . import views


app_name = AccountsConfig.name

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]