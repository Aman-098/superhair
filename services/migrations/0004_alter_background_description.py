# Generated by Django 5.0.6 on 2024-06-05 19:04

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]