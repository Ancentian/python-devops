from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
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
def employees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'base/employees.html', context)

@login_required(login_url='login')
def addEmployee(request):
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
                return redirect('employees')
            except Exception as e:
                messages.error(request, f'An error occurred during registration: {str(e)}')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form': form}
    return render(request, 'base/add-employee.html', context)

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

def users(request):
    userForm = MyUserCreationForm()
    users = User.objects.all()
    
    if request.method == 'POST':
        userForm = MyUserCreationForm(data=request.POST)
        if userForm.is_valid():
            user = userForm.save(commit=False)
            user.username = user.username.lower()
            # Modify other user fields here if needed
            user.save()
            messages.success(request, 'User registered successfully')
            return redirect('users')
        else:
            # Include form errors in the context to display them in the template
            context = {'users': users, 'userForm': userForm}
            return render(request, 'base/users/index.html', context)
         # Add a return statement here to return an HttpResponse object
    context = {'users': users, 'userForm': userForm}
    return render(request, 'base/users/index.html', context)

def editUser(request):
    if request.method == 'GET':
        user_id = request.GET.get('id')
        user = get_object_or_404(User, id=user_id)
        data = {'id': user.id, 'username': user.username, 'name': user.name, 'email': user.email }
        return JsonResponse(data)

def updateUser(request):
    user_id = request.POST.get('id')
    user = get_object_or_404(User, id=user_id)

    # Update employee data based on form submission
    user.name = request.POST.get('name')
    user.username = request.POST.get('username')
    user.email = request.POST.get('email')
    # Update other fields similarly
    user.save()

    return JsonResponse({'message': 'User updated successfully'})

def logoutUser(request):
    logout(request)
    return redirect('login')

def deleteItem(request, pk):
    try:
        item = User.objects.get(id=pk)
    except User.DoesNotExist:
        return HttpResponse('Item not found', status=404)
    
    # Check if the current user is authorized to delete the employee
    if request.user != item.user:
        return HttpResponse('You are not allowed here!!', status=403)
    
    if request.method == 'POST':
        item.delete()
        return redirect('employees')  
    
    context = {
        'obj': item
    }
    return render(request, 'base/delete.html', context)

def delete_user(request, pk):
    item = get_object_or_404(User, pk=pk)
    item.delete()
    return JsonResponse({'message': 'User deleted successfully.'})
