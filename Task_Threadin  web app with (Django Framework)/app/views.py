from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest



def home(request):
    """home view"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'year':datetime.now().year
        }
    )



def allTask(request):
    """Renders all Tasks created by Users."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/allTasks.html',
        {
            'title':'All Tasks (Current, Completed & Deleted)',
            'year':datetime.now().year,
        }
    )



def createTask(request):
    """Renders the create Task page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/createTask.html',
        {
            'title':'Create Your Task ',
            
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about app page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About details',
            'message':'Olwethu Theo Nyondo (Full Stack Developer) ',
            'year':datetime.now().year,
        }
    )


def currentTask(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/currentTask.html',
        {
            'title': 'Current Task',
            'year': datetime.now().year,
        }
          
    )


def userEditDetails(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewRegDetails.html',
        {
            'title': 'User Edit/ View Details',
            'message': 'My User Details',
            'year': datetime.now().year,
        }
          
    )



def registerForm(request):
    assert isinstance(request,HttpRequest)
    return render(request,'app/registrationForm.html',
                  {
                    'title': 'Custom User Registration Form',
                    'year': datetime.now().year,
                    }
                  )

def submit(request):
    assert isinstance(request,HttpRequest)
    obj = createTask()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.checkbox = request.GET['checkbox']
    obj.save()
    myDict={
        'allTasks': createTask.objects.all()
        
        }
    return render(request,'app/allTasks.html',context=myDict)