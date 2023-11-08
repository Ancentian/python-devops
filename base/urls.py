from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),    
    
    path('home/', views.home, name="home"),
    path('users/', views.users, name="users"),
    path('add-user/', views.addUser, name="add-user"),
    path('user-profile/', views.userProfile, name="user-profile"),
    path('delete-user/<str:pk>/', views.deleteUser, name="delete-user"),
    path('logout-user/', views.logoutUser, name="logout-user"),
]
