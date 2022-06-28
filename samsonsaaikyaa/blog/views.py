from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Post
 
class PostCreateView(CreateView):

    model = Post
    field = [
        "__all__"
    ]
    success_url: reverse_lazy("blog:all")
 
class PostListView(ListView):

    model = Post

class PostDetailView(DetailView):
    model: Post

class PostUpdateView(UpdateView):
    model: Post
    field = [
        "__all__"
    ]
    success_url: reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model: Post
    field = [
        "__all__"
    ]
    success_url: reverse_lazy("blog:all")