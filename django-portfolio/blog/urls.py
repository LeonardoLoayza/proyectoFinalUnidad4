from django.urls import path 
from .views import render_posts, post_detail

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'), # now, if we go to /blog/ we will render this
    path('<int:post_id>', post_detail, name="post_detail"), # using a dynamic url to show details of every post. For example: blog/12
]


