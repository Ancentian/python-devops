from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import User, Employee
from .forms import  EmployeeForm, UserForm, MyUserCreationForm

# Create your views here.

def loginUser(request):
    # page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User Does Not Exist!')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password Does Not Exist!')
            
    context = {}
    return render(request, 'base/auth/login.html', context)

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def users(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'base/users.html', context)

@login_required(login_url='login')
def addUser(request):
    # form = EmployeeForm()
    # if request.method == 'POST':
    #     form = EmployeeForm(data=request.POST)
    #     if form.is_valid():
    #         employee = form.save(commit=False)
    #         employee.email = employee.email.lower()
    #         employee.save()
    #         return redirect('users')
    #     else:
    #         messages.error(request, 'An Error Occured During registration')  
    # context = {'form' : form}
    # return render(request, 'base/add-user.html', context)

    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(data=request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.email = employee.email.lower()
            # You can check if the data is saved successfully here
            try:
                employee.save()
                messages.success(request, 'User added successfully')
                return redirect('users')
            except Exception as e:
                messages.error(request, f'An error occurred during registration: {str(e)}')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form': form}
    return render(request, 'base/add-user.html', context)

def registerUser(request):
    form = EmployeeForm
    if request.method == 'POST':
        form = EmployeeForm(data=request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.email = employee.email.lower()
            employee.save()
            return redirect('home')
        else:
            messages.error(request, 'An Error Occured During registration')
            
    context = {'form' : form}
    return render(request, 'base/login_register.html', context)

@login_required(login_url='login')
def userProfile(request ):
    context = {}
    return render(request, 'base/profile.html', context)

def deleteUser(request, pk):
    try:
        employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        return HttpResponse('Employee not found', status=404)
    
    # Check if the current user is authorized to delete the employee
    if request.user != employee.user:
        return HttpResponse('You are not allowed here!!', status=403)
    
    if request.method == 'POST':
        employee.delete()
        return redirect('users')  
    
    context = {
        'obj': employee
    }
    return render(request, 'base/delete.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
