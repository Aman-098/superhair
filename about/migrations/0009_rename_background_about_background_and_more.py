# Generated by Django 5.0.6 on 2024-06-06 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_alter_background_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Background',
            new_name='About_Background',
        ),
        migrations.RenameModel(
            old_name='Content',
            new_name='About_Content',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='About_Images',
        ),
    ]
