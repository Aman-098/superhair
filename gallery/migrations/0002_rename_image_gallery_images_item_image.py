# Generated by Django 5.0.6 on 2024-06-06 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery_images',
            old_name='image',
            new_name='item_image',
        ),
    ]
