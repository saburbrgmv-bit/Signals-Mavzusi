from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
  model = Post
  template_name = 'posts.html'
  context_object_name = 'posts'

class PostCreateView(CreateView):
  model = Post
  template_name = 'create.html'
  success_url = reverse_lazy('home')

class PostUpdateView(UpdateView):
  moel = Post
  template_name = 'update.html'
  success_url = reverse_lazy('home')

class PostDeleteView(DeleteView):
  model = Post
  template_name = 'delete.html'
  success_url = reverse_lazy('home')