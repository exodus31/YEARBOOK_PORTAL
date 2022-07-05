from tkinter import CASCADE
from django.db import models

# Create your models here.

class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    img = models.ImageField(blank=False, null=False, default=None)    
    year = models.IntegerField(default=0)
    username = models.CharField(max_length=100, default='x')    

    def __str__(self):
        return self.fname + ' ' + self.lname

class StudentGallery(models.Model):
    gimg = models.ImageField(blank=False, null=False)

    