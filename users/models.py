from django.db import models
from django.contrib import auth

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)