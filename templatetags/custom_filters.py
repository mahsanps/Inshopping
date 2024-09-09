from django import template

register = template.Library()

@register.filter
def is_available(product):
    return any(variation.quantity >= 1 for variation in product.variations.all())
