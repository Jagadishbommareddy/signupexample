from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User, null= True, on_delete=models.SET_NULL)
    email = models.EmailField()
    description = models.CharField(max_length= 255)

admin.site.register(Signup)