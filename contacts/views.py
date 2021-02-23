from django.contrib import messages
# from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Contact
from listings.models import Listing


def contact(request):
    user = request.user
    listing_id = request.POST['listing_id']
    listing = Listing.objects.get(pk=listing_id)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                listing=listing,
                user=user,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, 'Your request has been submitted, a realtor will get back to you soom')
        else:
            print('no valid')
            messages.error(request, 'Something went wrong, try again!')
            
    return redirect(listing)
