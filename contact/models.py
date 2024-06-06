from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Contact_Background(models.Model):
    background_image=models.ImageField(upload_to='contact/background_image')
    title=models.CharField(max_length=100)


    def __str__(self):
        return self.title
    
class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    
class Body(models.Model):
    title=models.CharField(max_length=100)
    description=HTMLField(default='')

    def __str__(self):
        return self.title
    
class ContactFormSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.CharField(max_length=20)
    comments = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.timestamp}"
