from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
# Create your views here.
from blog.forms import PostForm
from blog.models.post import PostModel
from blog.models.comentario import ComentarioModel
from blog.models.categoria import CategoriaBlogModel


# class HomeTemplateView(TemplateView):
#     template_name = 'blog/index.html'


class PostIndex(ListView):
    template_name = 'blog/postagem/lista.html'
    model = PostModel
    context_object_name = 'posts'

class PostDetalhes(DetailView):
    template_name = 'blog/postagem/detalhe.html'
    model = PostModel
    context_object_name = 'post'


