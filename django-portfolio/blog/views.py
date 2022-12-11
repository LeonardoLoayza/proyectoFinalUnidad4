from django.shortcuts import render, get_object_or_404
from .models import Post

def render_posts(request): # this is going to render the post html
    posts = Post.objects.all()    
    
    return render(request, 'posts.html', {'posts' : posts})

def post_detail(request, post_id): 
    post = get_object_or_404(Post,pk=post_id) # is going to search inside db.sqlite3, in case it exists we return something 
    return render(request, 'post_detail.html', {'post' : post } ) # and we send it to our post_detail.html
    