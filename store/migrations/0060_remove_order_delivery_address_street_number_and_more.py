# Generated by Django 5.0.6 on 2024-07-14 09:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0059_shop_image_alter_orderdelivery_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_address_street_number',
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='accountNumber',
            field=models.CharField(default='', max_length=200, verbose_name='accountNumber'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='bankName',
            field=models.CharField(default='', max_length=200, verbose_name='bankName'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='cartNumber',
            field=models.CharField(default='', max_length=200, verbose_name='cartNumber'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(default='', max_length=400, verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='order',
            name='account',
            field=models.ForeignKey(blank=True, db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='account'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address_city',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address_postcode',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='postCode'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address_state',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address_street_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='streetName'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address_suburb',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='suburb'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address_unit_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='unitNumber'),
        ),
        migrations.AlterField(
            model_name='order',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='mobileNumber'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_discount',
            field=models.FloatField(verbose_name='totalDiscount'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(verbose_name='totalPrice'),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='status',
            field=models.CharField(choices=[('SUBMITTED', 'Submitted'), ('PENDING', 'Pending'), ('CANCELLED', 'Cancelled'), ('FAILED', 'Failed'), ('DISPATCHED', 'Dispatched'), ('DELIVERING', 'Delivering'), ('DELIVERED', 'Delivered')], default='registered', max_length=200, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='tracking_number',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='trackingNumber'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='discount',
            field=models.FloatField(verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='total_price',
            field=models.FloatField(verbose_name='totalPrice'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='media/static/images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='isactive',
            field=models.BooleanField(default=True, verbose_name='isactive'),
        ),
        migrations.AlterField(
            model_name='product',
            name='madeIn',
            field=models.CharField(max_length=200, verbose_name='madeIn'),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(max_length=200, verbose_name='material'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='productName'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productCode',
            field=models.CharField(max_length=500, verbose_name='productCode'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.shop', verbose_name='shop'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.subcategory', verbose_name='Subcategory'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='media/static/images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.color', verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='size',
            field=models.CharField(default='', max_length=400, verbose_name='size'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='account'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(max_length=400, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='contact',
            field=models.CharField(max_length=20, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/static/images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='instagramId',
            field=models.URLField(verbose_name='instagramId'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='store_name',
            field=models.CharField(max_length=400, verbose_name='storename'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subname',
            field=models.CharField(max_length=200, verbose_name='Subcategory'),
        ),
    ]
