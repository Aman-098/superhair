# Generated by Django 4.2.5 on 2024-06-05 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_images_remove_body_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='images',
            new_name='image',
        ),
    ]
