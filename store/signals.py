from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import os
from .models import ShopImage, Shop, Product, SubCategory, ProductImage, Blog
from django.conf import settings

def convert_image_to_webp(image_field):
    try:
        image_path = image_field.path
        if os.path.exists(image_path):
            print(f"Converting image: {image_path}")
            img = Image.open(image_path).convert("RGB")  # تبدیل به RGB برای جلوگیری از مشکلات کانال رنگ
            webp_path = os.path.splitext(image_path)[0] + ".webp"
            img.save(webp_path, "WEBP", quality=80)
            print(f"WebP saved at: {webp_path}")
            return webp_path
    except Exception as e:
        print(f"Error converting image to WebP: {e}")
    return None

@receiver(post_save, sender=ShopImage)
@receiver(post_save, sender=Shop)
@receiver(post_save, sender=Product)
@receiver(post_save, sender=SubCategory)
@receiver(post_save, sender=ProductImage)
@receiver(post_save, sender=Blog)
def optimize_images(sender, instance, **kwargs):
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

    for field_name in image_fields:
        image_field = getattr(instance, field_name)
        if image_field and os.path.exists(image_field.path):
            # فقط اگر فایل تغییر کرده باشد، عملیات تبدیل را اجرا کنید
            webp_path = convert_image_to_webp(image_field)
            if webp_path:
                # آپدیت مسیر فیلد بدون ذخیره مجدد رکورد
                image_field.name = os.path.relpath(webp_path, settings.MEDIA_ROOT)
                instance.save(update_fields=[field_name])  # به‌روزرسانی فیلد فقط برای ذخیره مسیر جدید
