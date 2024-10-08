from django import template
from django.utils.translation import gettext as _

register = template.Library()

@register.filter
def is_available(product):
    return any(variation.quantity >= 1 for variation in product.variations.all())






