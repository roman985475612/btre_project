from django import forms
from django.core.exceptions import ValidationError

from .models import Contact
from listings.models import Listing


class ContactForm(forms.Form):
    listing_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    listing_title = forms.CharField(
        label='Property',
        disabled=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        listing_id = cleaned_data.get('listing_id')
        listing = Listing.objects.get(pk=listing_id)
        has_contacted = Contact.objects.filter(email=email, listing=listing)
        if has_contacted:
            raise ValidationError('')
