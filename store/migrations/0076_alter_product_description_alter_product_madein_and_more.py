# Generated by Django 5.0.6 on 2024-08-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0075_remove_productvariation_variation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='madeIn',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='madeIn'),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='material'),
        ),
    ]
