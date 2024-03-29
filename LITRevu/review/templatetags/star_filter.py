from django import template

register = template.Library()


@register.filter
def stars(value):

    if value is not [None, ""]:
        if value > 0 and value < 6:
            return '★' * int(value)
        else:
            return ''
