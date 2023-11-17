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
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    fname = models.CharField(max_length=200, null=False)
    lname = models.CharField(max_length=200, null=False)
    email = models.EmailField(unique=True)
    employee_id =models.CharField(max_length=20, unique=True, null=False)
    joining_date = models.DateField(null=True)
    phone_no = models.CharField(max_length=15, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=100, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    avatar = models.ImageField(null=True, default="user.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']
    
    def __str__(self):
        return self.fname
    
    def get_department_name(self):
        return self.department.name if self.department else "--"
    