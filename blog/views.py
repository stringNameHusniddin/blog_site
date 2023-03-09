from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class HomePage(ListView):
    model = Post
    template_name = 'home.html'

class DetailPage(DetailView):
    model = Post
    template_name = 'blog_detail.html'

class NewBlogPage(CreateView):
    model = Post
    template_name = 'new_blog.html'
    fields = ['title', 'author', 'body']

class UpdatePage(UpdateView):
    model = Post
    template_name = 'update_blog.html'
    fields = ['title', 'body']

class DeletePage(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')