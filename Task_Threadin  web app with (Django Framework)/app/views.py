from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest



def homeView(request):
    """Renders all Tasks created by Users."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'year':datetime.now().year,
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
            'message':'Please create your tasks here',
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
            'message': 'Tasks Currently',
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