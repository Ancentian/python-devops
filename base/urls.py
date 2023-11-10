from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logoutUser"),    
    
    path('home/', views.home, name="home"),
    path('employees/', views.employees, name="employees"),
    path('users/', views.users, name="users"),
    path('add-employee/', views.addEmployee, name="add-employee"),
    
    path('edit-user/', views.editUser, name="edit-user"),
    path('update-user/', views.updateUser, name="update-user"),
    
    path('user-profile/', views.userProfile, name="user-profile"),
    path('delete-item/<str:pk>/', views.deleteItem, name="delete-item"),
    path('delete-user/<str:pk>/', views.delete_user, name="delete-user"),
]
