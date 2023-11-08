from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="user.jpg")
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = []
    
class Employee(models.Model):
    fname = models.CharField(max_length=200, null=False)
    lname = models.CharField(max_length=200, null=False)
    email = models.EmailField(unique=True)
    employee_id =models.CharField(max_length=20, unique=True, null=False)
    joining_date = models.DateField(null=True)
    phone_no = models.CharField(max_length=15, null=True)
    role = models.CharField(max_length=50, null=True)
    avatar = models.ImageField(null=True, default="user.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.fname