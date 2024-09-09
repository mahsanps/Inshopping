# Generated by Django 5.0.4 on 2024-05-12 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0042_remove_orderitem_quantity_item_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('images', models.ImageField(upload_to='media/static/images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
