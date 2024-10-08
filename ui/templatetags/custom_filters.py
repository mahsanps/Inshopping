from django import template
from django.template.defaultfilters import floatformat
from django.contrib.humanize.templatetags.humanize import intcomma
from django import template
from django.utils.translation import gettext as _






register = template.Library()

@register.filter

def custom_price_format(value):
    try:
        # Convert to float to handle both integers and decimals
        value = float(value)
        # Format the value with commas
        formatted_value = "{:,.2f}".format(value).rstrip('0').rstrip('.')
        return formatted_value
    except (ValueError, TypeError):
        # In case the value is not a number, return it as is
        return value
    
    
