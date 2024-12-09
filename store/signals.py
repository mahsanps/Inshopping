from django.db.models.signals import post_save
from django.dispatch import receiver
from inshopping.tasks import convert_image_to_webp
from .models import Product, ProductImage

@receiver(post_save, sender=Product)
def optimize_product_image(sender, instance, **kwargs):
    if instance.image:
        convert_image_to_webp.delay('Product', instance.id, 'image')

@receiver(post_save, sender=ProductImage)
def optimize_product_image_instance(sender, instance, **kwargs):
    if instance.image:
        convert_image_to_webp.delay('ProductImage', instance.id, 'image')
