# Generated by Django 5.0.6 on 2024-05-11 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0037_orderitem_product_delete_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
    ]
