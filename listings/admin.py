from django.contrib import admin

from .models import Listing, Photo, State


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)
    # list_display_links = ('code', 'name',)
    # list_editable = ('code', 'name',)


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'title',
        'is_published',
        'state2',
        'price',
        'list_date',
        'realtor',
        'badrooms',
    )
    
    list_display_links = (
        'id',
        'title'
    )
    
    list_filter = (
        'realtor',
    )
    
    list_editable = (
        'is_published',
        'badrooms',
        'state2',
    )
    
    search_fields = (
        'title',
        'description',
        'address',
        'city',
        'zipcode',
        'price'
    )
    
    list_per_page = 10
    

admin.site.register(Photo)
