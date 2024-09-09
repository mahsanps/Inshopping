# Generated by Django 5.0.6 on 2024-07-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0062_alter_product_description_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/static/images/'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='bankName',
            field=models.CharField(default='', max_length=200, verbose_name='BankName'),
        ),
    ]
