from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Background_Images(models.Model):
    image=models.ImageField(upload_to='book-it/background_image')
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Body_Content(models.Model):
    title=models.CharField(max_length=100)
    description = HTMLField()

    def __str__(self):
        return self.title


class Book_Appointment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=20)
    email = models.EmailField()
    style_needed = models.CharField(max_length=255)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    street_address = models.CharField(max_length=255)
    like_website = models.CharField(max_length=10)
    find_us = models.CharField(max_length=255)
    comments = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.appointment_date} {self.appointment_time}"
