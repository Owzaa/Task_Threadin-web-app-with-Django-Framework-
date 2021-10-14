"""
Definition of urls for Task_Threadin__web_app_with__Django_Framework_.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit',views.submit, name='submit'),
    path('registerForm/', views.registerForm,name='registerForm'),
    path('currentTask/', views.currentTask, name='currentTask'),
    path('allTask/', views.allTask, name='allTask'),
    path('createTask/', views.createTask, name='createTask'),
    path('userEditDetails/', views.userEditDetails, name='userEditDetails'),
    path('about/', views.about, name='about'),
    path('login/',LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Login',
             }
         ),   name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('admin/', admin.site.urls),
]   
