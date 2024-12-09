from store.models import Shop, ShopImage, Product, ProductImage, SubCategory, Blog
from celery import shared_task
from PIL import Image
import os

@shared_task

def convert_image_to_webp(model_name, instance_id, field_name):
    # به دست آوردن مدل بر اساس نام مدل
    model_map = {
        'ShopImage': ShopImage,
        'Shop': Shop,
        'Product': Product,
        'SubCategory': SubCategory,
        'ProductImage': ProductImage,
        'Blog': Blog,
    }
    
    model = model_map.get(model_name)
    if model:
        try:
            # گرفتن نمونه مدل
            instance = model.objects.get(id=instance_id)
            image_field = getattr(instance, field_name)

            if image_field and os.path.exists(image_field.path):
                # باز کردن تصویر
                image = Image.open(image_field.path)

                # تعیین مسیر جدید برای ذخیره تصویر WebP
                webp_path = image_field.path.rsplit('.', 1)[0] + ".webp"
                
                # ایجاد پوشه‌ای که تصویر WebP در آن ذخیره شود اگر وجود نداشته باشد
                webp_dir = os.path.dirname(webp_path)
                if not os.path.exists(webp_dir):
                    os.makedirs(webp_dir)
                
                # تبدیل و ذخیره تصویر به فرمت WebP
                image.save(webp_path, 'WEBP')
                
                # به روزرسانی مسیر جدید تصویر در مدل
                setattr(instance, field_name, webp_path)
                instance.save()

        except Exception as e:
            print(f"Error during image conversion: {e}")
