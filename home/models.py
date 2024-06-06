from django.db import models

# Create your models here.

class Header(models.Model):
    background_image = models.ImageField(upload_to='home/header_background_images' ,default="")
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title

class Service_content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='home/services_images')

    def __str__(self):
        return self.title

    
class WhatsHappening(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='') 
    image = models.ImageField(upload_to='home/whats_happening')

    def __str__(self):
        return self.title



