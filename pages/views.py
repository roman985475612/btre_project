from django.shortcuts import render

from .models import Service, UserField
from listings.models import Listing, State
from realtors.models import Realtor
from .choices import bedrooms, prices, states


def index(request):
    return render(request, 'pages/index.html', {
        'title': 'Home',
        'listings': Listing.objects.get_published()[:3],
        'bedrooms': bedrooms,
        'prices': prices,
        'states': State.objects.all(),
        'services': Service.objects.all()[:3],
    })


def about(request):
    queryset = UserField.objects.all()

    user_fields = {}
    for record in queryset:
        user_fields[record.name] = record.value
    print(user_fields)

    return render(request, 'pages/about.html', {
        'title': 'About',
        'sub_title': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, pariatur!',
        'realtors': Realtor.objects.all(),
        'mvp_realtors': Realtor.objects.get_mvp(),
        'user_fields': user_fields,
    })