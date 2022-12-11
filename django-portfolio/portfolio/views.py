from django.shortcuts import render
from .models import Project # from this models.py we import the model Project cause we want to make a query and get all the projects to show in home.html

# we're going to show all the projects in this view
def home(request): 
    projects = Project.objects.all() # to be able to use this data in the html, we use a dictionary and we proceed 
    
    return render(request, 'home.html', {'projects': projects}) 