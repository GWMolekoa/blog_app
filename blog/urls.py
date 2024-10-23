from django.urls import path
from .views import Blog, Posts, CreatePosts

urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('blog-post/<int:pk>', Posts.as_view(), name='posts'),
    path('create-post/', CreatePosts.as_view(), name='create-post'),
]  