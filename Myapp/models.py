from atexit import register
from datetime import date
import email
from email.policy import default
import profile
from statistics import mode
from unicodedata import name
from django.db import models
import random as r

from django.forms import EmailField
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

class Department(models.Model):
    name=models.CharField(max_length=30)
    headdepartment=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=13)
    no_of_student=models.IntegerField()
    dep_date=models.DateField(null=True)
    date=models.DateField(auto_now_add=True)
    varify=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    approve_by = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name

class All_Course(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE)
    coname=models.CharField(max_length=50)
    coduration=models.CharField(max_length=30)
    coprice=models.IntegerField()
    codepartment=models.ForeignKey(Department,on_delete=models.CASCADE)
    codiscription=models.TextField(max_length=100)
    coyear=models.IntegerField()
    copic=models.ImageField(upload_to='course pic',default='python.png')
    covarify=models.BooleanField(default=False)
    coreject=models.BooleanField(default=False)
    approve_by = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.coname

# class Student(models.Model):
#     choices = (('male','male'),('female','female'),('other','other'))

#     fname=models.CharField(max_length=30)
#     username=models.CharField(unique=True)
#     email=models.EmailField(unique=True)
#     Adhaar=models.IntegerField(max_length=12,unique=True)
#     address=models.TextField()
#     mobile=models.CharField(max_length=13)
#     dob=models.DateField()
#     stupic=models.ImageField(upload_to='Student Pic',default=logo)
#     postcode=models.CharField(max_length=30)
#     department=models.ForeignKey(Registe,on_delete=models.CASCADE)
#     dis=models.TextField(max_length=100)
#     gender=models.CharField(max_length=20,choices=choices)
#     country=models.CharField(max_length=30)
#     state=models.CharField(max_length=30)
#     city=models.CharField(max_length=30)
#     date_of_join=models.DateField(auto_now_add=True)
#     
#     def __str__(self):
#         return self.username

# class Library(models.Model):
#     subject=models.CharField(max_length=30)
#     department=models.ForeignKey(Registe,on_delete=models.CASCADE)
#     Author=models.CharField(max_length=30)
#     price=models.IntegerField()
#     puyear=models.IntegerField()
#     frontpic=models.ImageField(upload_to='Book pic',default='python.png')
#     def __str__(self):
#         return self.subject



# class Enquiry(models.Model):
#     name=models.CharField(max_length=30)
#     email=models.EmailField(unique=True)
#     subject=models.CharField(max_length=30)
#     mobile=models.CharField(max_length=13)
#     des=models.TextField(max_length=200)
#     enq_time = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.name

