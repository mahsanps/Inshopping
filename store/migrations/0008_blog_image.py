# Generated by Django 5.0.6 on 2024-11-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_homepagecontent_blog_is_deleted_alter_blog_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to='images/', verbose_name='Image'),
        ),
    ]
