from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class About_Background(models.Model):
    background_image = models.ImageField(upload_to='about/header_background_images' ,default="")
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    
class About_Images(models.Model):
    image=models.ImageField(upload_to="about/images")

    

class About_Content(models.Model):
    title= models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description = HTMLField()

    def __str__(self):
        return self.title

