# Generated by Django 5.0.6 on 2024-08-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0067_remove_productimage_is_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('authority', models.CharField(max_length=255, unique=True)),
                ('ref_id', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
