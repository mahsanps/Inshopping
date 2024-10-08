# Generated by Django 5.0.6 on 2024-10-08 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_shopauth_token_expiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='shopauth',
            name='token_expiry',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 7, 15, 3, 12, 714066, tzinfo=datetime.timezone.utc)),
        ),
    ]
