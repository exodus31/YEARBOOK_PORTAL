from tkinter import CASCADE
from django.db import models

# Create your models here.

class Year(models.Model):
    year = models.CharField(max_length=4,null=False, blank=False)    

    def __str__(self):
        return self.year

class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    img = models.ImageField(blank=False, null=False)
    age = models.IntegerField()
    year = models.ForeignKey(Year, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.fname + ' ' + self.lname