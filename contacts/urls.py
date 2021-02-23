from django.urls import path

from .apps import ContactsConfig
from .views import contact

app_name = ContactsConfig.name

urlpatterns = [
    path('contact', contact, name="contact"),
]
