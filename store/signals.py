from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import os
from .models import ShopImage, Shop, Product, SubCategory, ProductImage, Blog
from django.conf import settings

# تابع برای تبدیل تصاویر به فرمت WebP
def convert_image_to_webp(image_field):
    image_path = image_field.path
    if os.path.exists(image_path):
        # باز کردن و تبدیل تصویر به WebP
        img = Image.open(image_path).convert("RGB")  # تبدیل به RGB در صورتی که تصویر CMYK باشد
        webp_path = os.path.splitext(image_path)[0] + ".webp"
        img.save(webp_path, "WEBP", quality=80)  # کیفیت 80 درصد
        return webp_path
    return None

@receiver(post_save, sender=ShopImage)
@receiver(post_save, sender=Shop)
@receiver(post_save, sender=Product)
@receiver(post_save, sender=SubCategory)
@receiver(post_save, sender=ProductImage)
@receiver(post_save, sender=Blog)
def optimize_images(sender, instance, created, **kwargs):
    if created:  # اجرا فقط در زمان ایجاد رکورد
        if sender == ShopImage:
            image_fields = ['banner_image1', 'banner_image2', 'banner_image3']
        elif sender == Shop:
            image_fields = ['image']
        elif sender == Product:
            image_fields = ['image']
        elif sender == SubCategory:
            image_fields = ['image']
        elif sender == ProductImage:
            image_fields = ['image']
        elif sender == Blog:
            image_fields = ['image']
        else:
            return

        for field_name in image_fields:
            image_field = getattr(instance, field_name, None)
            if image_field and hasattr(image_field, 'path') and os.path.exists(image_field.path):
                webp_path = convert_image_to_webp(image_field)
                if webp_path:
                    # به‌روزرسانی مسیر فایل فیلد تصویر به WebP بدون حلقه بازگشتی
                    setattr(instance, field_name, os.path.relpath(webp_path, settings.MEDIA_ROOT))
        instance.save(update_fields=image_fields)
