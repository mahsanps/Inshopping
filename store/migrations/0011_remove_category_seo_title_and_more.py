# Generated by Django 5.0.6 on 2024-11-21 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_homepagecontent_seo_keywords_alter_blog_seo_keywords_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='seo_title',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='seo_title',
        ),
    ]
