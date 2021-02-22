from django.urls import path

from . import views
from .apps import ContactsConfig

app_name = ContactsConfig.name

urlpatterns = [
    path('contact', views.contact, name="contact"),
]
