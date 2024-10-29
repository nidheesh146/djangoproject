# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Addcourse(models.Model):
    coursename=models.CharField(max_length=255)
    coursefee=models.IntegerField(null=True)
class Student(models.Model):
    course=models.ForeignKey(Addcourse,on_delete=models.CASCADE,null=True)
    stdname=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField(null=True)
    date=models.DateField()
class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=255,null=True)
    username=models.CharField(max_length=255,null=True)
    password=models.CharField(max_length=255,null=True)
    email=models.EmailField(null=True)
    course=models.ForeignKey(Addcourse,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255,null=True)
    age=models.IntegerField(null=True)
    contact=models.CharField(max_length=255,null=True)
    image=models.ImageField(upload_to='image/',blank=True)
    