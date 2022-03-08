from atexit import register
import email
from email.policy import default
import profile
from django.db import models
import random as r
pic=['logo1.jpg','logo2.png','logo3.jpg','logo4.png','logo5.png','logo6.png','logo7.png','logo8.png','logo9.png','logo10.png','logo11.png','logo12.png','logo13.png','logo14.png','logo15.png','logo16.png']
logo=r.choice(pic)
# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=13)
    gender=models.CharField(max_length=6)
    email=models.EmailField(unique=True)
    address=models.TextField(max_length=60)
    password=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='Profile Pic',default=logo)

    def __str__(self):
        return self.name


class All_Course(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE)
    coname=models.CharField(max_length=50)
    coduration=models.CharField(max_length=30)
    coprice=models.IntegerField()
    codepartment=models.CharField(max_length=30)
    codiscription=models.TextField(max_length=100)
    coyear=models.IntegerField()
    copic=models.ImageField(upload_to='course pic',default='python.png')
    covarify=models.BooleanField(default=False)
    coreject=models.BooleanField(default=False)
    approve_by = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.coname