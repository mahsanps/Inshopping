# Generated by Django 4.2.1 on 2023-09-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_remove_product_colors_remove_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
