from django.db import models

# Create your models here.


class Content(models.Model):
    bg_image=models.ImageField(upload_to='gallery/background_image')
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    
    
class Gallery_Images(models.Model):
    item_image=models.ImageField(upload_to='gallery/images')

