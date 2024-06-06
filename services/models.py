from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Background_content(models.Model):
    background_image=models.ImageField(upload_to='services/background_image')
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description=HTMLField()

    def __str__(self):
        return self.title
    
    

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')


    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)  # Storing price as string to accommodate "and Up" or other text

    def __str__(self):
        return self.name
