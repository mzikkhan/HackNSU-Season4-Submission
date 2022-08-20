from hashlib import blake2b
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    userid=models.CharField(max_length=40,null=False,blank=False,verbose_name="Student ID",primary_key=True)
    name=models.CharField(max_length=50,null=False,blank=False,verbose_name="Student Name")
    email=models.EmailField(max_length=50,null=False,blank=False,verbose_name="Email")
    
    def __str__(self):
        return self.userid
class UserPic(models.Model):
    userid=models.OneToOneField(Users,null=True,on_delete=models.CASCADE)
    picture=models.ImageField(null=True,blank=True)
class Complain(models.Model):
    bully_id = models.CharField(max_length=40, null=False, blank=False, verbose_name="Bully ID")
    abuseDescription=models.CharField(max_length=1000,null=False,blank=False,verbose_name="Complain Description")
    links=models.URLField(max_length=200,null=False,blank=False,verbose_name="Links")
    anonymity=models.CharField(max_length=20,null=False,blank=False,verbose_name="Anonymity")
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bully_id