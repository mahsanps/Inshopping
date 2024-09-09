# Generated by Django 5.0.6 on 2024-07-01 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0058_alter_subcategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/static/images/'),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='status',
            field=models.CharField(choices=[('SUBMITTED', 'Submitted'), ('PENDING', 'Pending'), ('CANCELLED', 'Cancelled'), ('FAILED', 'Failed'), ('DISPATCHED', 'Dispatched'), ('DELIVERING', 'Delivering'), ('DELIVERED', 'Delivered')], default='registered', max_length=200),
        ),
    ]
