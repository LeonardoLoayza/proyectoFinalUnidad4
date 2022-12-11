from django.db import models
from django.db.models.fields import CharField, URLField, TextField, DateField
from django.db.models.fields.files import ImageField 
import datetime 
# we import the fields, URLField is basically a charfield for a URL


class Post(models.Model):
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to='blog/images') # basically this is going to create a folder inside media with name 'blog'  
    date = DateField(datetime.date.today)
    tags = CharField(max_length=150)
    
     