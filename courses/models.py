from django.db import models

# Create your models here.


class Student(models.Model):
    student_id= models.IntegerField()
    student_name= models.CharField(max_length=20)
    student_email = models.CharField(max_length=30)
    batch = models.IntegerField()
    course = models.CharField(max_length=30)


class Info(models.Model):
    first_name=models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    batch=models.IntegerField()    
    password = models.CharField(max_length=30)
    re_password= models.CharField(max_length=30)
    text = models.CharField(max_length=100)
    payment= models.DecimalField(max_digits=6,decimal_places=2)
    email = models.EmailField(max_length=20)
    django= models.BooleanField()
