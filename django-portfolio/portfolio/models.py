from django.db import models
from django.db.models.fields import CharField, URLField # we import the fields, URLField is basically a charfield for a URL
from django.db.models.fields.files import ImageField # we're going to save images as well

# define what I want to save in the database, the model
# ctrl + space 

class Project (models.Model): # always use 'model.Model' 
    title = CharField(max_length=100) 
    description = CharField(max_length=250)
    image = ImageField(upload_to = 'portfolio/images/') # inside portfolio app there will be a folder where the images will be stored
    url = URLField(blank=True) 
    tags = CharField(max_length=150)
    
