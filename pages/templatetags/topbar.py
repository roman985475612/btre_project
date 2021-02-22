from django import template

from pages.models import UserField

register = template.Library()


@register.inclusion_tag('inc/_topbar.html')
def show_topbar():
    user_fields = {}
    for field in UserField.objects.all():
        user_fields[field.name] = field.value
    return {'user_fields': user_fields}
