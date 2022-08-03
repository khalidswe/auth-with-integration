from pyexpat import model
from django.db import models

# Create your models here.

class User(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=30)
    Password = models.CharField(max_length=50)
    Images = models.ImageField(upload_to="img/")

class Image(models.Model):
    Imagename = models.CharField(max_length=30)
    Image = models.ImageField(upload_to="img/")