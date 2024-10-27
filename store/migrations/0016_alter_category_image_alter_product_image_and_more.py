# Generated by Django 5.0.6 on 2024-10-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_category_image_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='media/images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='media/images/', verbose_name='Images'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='banner_image1',
            field=models.ImageField(default='', upload_to='media/images/', verbose_name='banner-Image1'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='banner_image2',
            field=models.ImageField(default='', upload_to='media/images/', verbose_name='banner-Image2'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='banner_image3',
            field=models.ImageField(default='', upload_to='media/images/', verbose_name='banner-Image3'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(default='', upload_to='media/images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]