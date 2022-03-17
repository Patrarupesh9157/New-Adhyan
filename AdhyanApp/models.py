from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    address = models.TextField(max_length=150 )
    password = models.CharField(max_length=15)
    pic = models.FileField(upload_to='Profile Pic', default='avtar.png')
    
    def __str__(self):
        return self.email