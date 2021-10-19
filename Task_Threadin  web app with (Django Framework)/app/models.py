"""
Definition of models.
"""
from django.db import models
from .models import *

# Create your models here.
class createTask(models.Model):
    title = models.CharField(max_length=255)
    descrition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




class UserRegistration (models.Model):

    username = models.CharField(max_length=40)                             

    password = models.CharField(max_length=40)

    confirmpassword = models.CharField(max_length=40)

    firstname = models.CharField(max_length=40)

    surname = models.CharField(max_length=40)

    mobile = models.CharField(max_length=10)

    IDnumber = models.CharField(max_length=13)

    email = models.CharField(max_length=40)

    address = models.CharField(max_length=40)

    copyid = models.ImageField()
    
    proofofaddress = models.ImageField()


    class Meta:     
        db_table = "userregistration"


      
def WriteToExcel(AllTasks_data,DeletedTasks_data,QuedTasks_data, allTask=None):
    
    QuedTasks_data= QuedTasks.objects.all()
    DeletedTasks_data= DeletedTasks.objects.all()
    AllTasks_data= allTask.objects.all()
    

