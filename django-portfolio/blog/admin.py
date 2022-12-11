from django.contrib import admin
from .models import Post

admin.site.register(Post) # A simple way to make a form 

# be sure to use 'python manage.py makemigrations' and migrate the table
# basically to be able to create new posts in Blog