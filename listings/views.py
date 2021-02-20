from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Listing, State
from pages.choices import bedrooms as bedrooms_list, prices, states


def index(request):
    listings = Listing.objects.get_published()

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request, 'listings/listings.html', {
        'listings': paged_listings
    })


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    thumbs = listing.photo_set.all();
    return render(request, 'listings/listing.html', {
        'listing': listing,
        'thumbs': thumbs,
    })


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state2__code__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(badrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    paginator = Paginator(queryset_list, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request, 'listings/search.html', {
        'listings': paged_listings,
        'bedrooms': bedrooms_list,
        'prices': prices,
        'states': State.objects.all(),
        'values': request.GET
    })
