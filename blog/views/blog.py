from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'blog/index.html'
