from django.db import models

# Create your models here.

from django.db import models
import datetime

# Create your models here.


class student(models.Model):
    firstname = models.CharField(max_length=200,null=True)
    lastname = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    age = models.IntegerField(null=True)
    phonenumber = models.IntegerField()
    address =  models.CharField(max_length=200,null=True)
    department = models.CharField(max_length=200,null=True) 
    username = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.username
    
class teacher(models.Model):
    firstname = models.CharField(max_length=200,null=True)
    lastname = models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=200,null=True)
    password = models.IntegerField()
    email = models.CharField(max_length=200,null=True)
    age = models.IntegerField(null=True)
    phonenumber = models.IntegerField()
    address =  models.CharField(max_length=200,null=True)
    department =  models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.username

    approved = models.BooleanField(default=False)


class leave(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255,null=True)
    date = models.DateField(default=datetime.date.today)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
