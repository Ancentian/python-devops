from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import  User, Employee
# from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2', 'avatar']

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['avatar','fname','lname', 'email', 'employee_id', 'joining_date', 'phone_no','role']
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email', 'bio']
        