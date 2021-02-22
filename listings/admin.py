from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Listing, Photo, State


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)


class PhotoInLine(admin.TabularInline):
    model = Photo


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    inlines = [PhotoInLine]
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
    
    list_display_links = ('id', 'title')
    list_filter = ('realtor', )
    
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


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('listing', 'title', 'get_photo')
    list_filter = ('listing',)
    search_fields = ('title',)
    list_per_page = 25

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')

