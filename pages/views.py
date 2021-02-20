from django.shortcuts import render

from listings.models import Listing, State
from realtors.models import Realtor
from .choices import bedrooms, prices, states


def index(request):
    return render(request, 'pages/index.html', {
        'listings': Listing.objects.get_published()[:3],
        'bedrooms': bedrooms,
        'prices': prices,
        'states': State.objects.all(),
    })


def about(request):
    return render(request, 'pages/about.html', {
        'realtors': Realtor.objects.all(),
        'mvp_realtors': Realtor.objects.get_mvp(),
    })