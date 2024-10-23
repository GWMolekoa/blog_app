from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.
class Blog(ListView):
    model = Post
    template_name = 'blog.html'

class Posts(DetailView):
    model = Post
    template_name = 'post.html'

class CreatePosts(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
   
