from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Service, UserField


@admin.register(UserField)
class UserFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    list_display_links = ('name', 'value')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('sort', 'title', 'show_icon')
    list_display_links = ('title', 'show_icon')
    list_editable = ('sort',)

    def show_icon(self, obj):
        return mark_safe(f'<i class="{obj.fa_icon_class} fa-2x"></i>')

    show_icon.short_description = 'Font awesome'
