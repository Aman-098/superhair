# Generated by Django 5.0.6 on 2024-06-06 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('telephone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('style_needed', models.CharField(max_length=255)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('street_address', models.CharField(max_length=255)),
                ('city_state_zipcode', models.CharField(max_length=255)),
                ('access_code', models.CharField(max_length=20)),
                ('like_website', models.CharField(max_length=10)),
                ('find_us', models.CharField(max_length=255)),
                ('comments', models.TextField()),
            ],
        ),
    ]
