from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''

@register.filter(name='sum')
def sum_filter(queryset, attribute):
    return sum(getattr(item, attribute) for item in queryset)