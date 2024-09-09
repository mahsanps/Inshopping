from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _





class OrderStatusChoices(TextChoices):
    SUBMITTED = "SUBMITTED", _("SUBMITTED")
    DELIVERING = "DELIVERING", _("DELIVERING")
    DELIVERED = "DELIVERED", _("DELIVERED")
    
    
class ProductVariationTypeChoices(TextChoices):
    PRODUCT = "PRODUCT"
    VARIATION = "VARIATION"