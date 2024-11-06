from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import os
from .models import Shop, Product, SubCategory, ProductImage
from django.conf import settings

# تابع برای تبدیل تصاویر به فرمت WebP
def convert_image_to_webp(image_field):
    image_path = image_field.path
    if os.path.exists(image_path):
        # باز کردن و تبدیل تصویر به WebP
        img = Image.open(image_path)
        webp_path = os.path.splitext(image_path)[0] + ".webp"
        img.save(webp_path, "WEBP", quality=80)  # کیفیت 80 درصد
        return webp_path
    return None

@receiver(post_save, sender=Shop)
@receiver(post_save, sender=Product)
@receiver(post_save, sender=SubCategory)
@receiver(post_save, sender=ProductImage)  # اضافه کردن ProductImage به سیگنال
def optimize_images(sender, instance, created, **kwargs):
    if created:  # اجرا فقط در زمان ایجاد رکورد
        if sender == Shop:
            image_fields = ['image', 'banner_image1', 'banner_image2', 'banner_image3']
        elif sender == Product:
            image_fields = ['image']  # فقط فیلد image در Product
        elif sender == SubCategory:
            image_fields = ['image']  # فیلد image در SubCategory
        elif sender == ProductImage:  # اضافه کردن فیلد image در ProductImage
            image_fields = ['image']

        for field_name in image_fields:
            image_field = getattr(instance, field_name)
            if image_field and os.path.exists(image_field.path):
                webp_path = convert_image_to_webp(image_field)
                if webp_path:
                    # به‌روزرسانی مسیر فایل فیلد تصویر به WebP بدون فراخوانی دوباره save()
                    image_field.name = os.path.relpath(webp_path, settings.MEDIA_ROOT)
                    # توجه: از ذخیره مجدد استفاده نکنید تا از حلقه بازگشتی جلوگیری شود
                    instance.save(update_fields=[field_name])  # فقط این فیلد را به‌روزرسانی می‌کنیم
