from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView, CreateView
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


# admin
class PostAdmin(CreateView):
    model = PostModel
    template_name = 'blog/postagem/criar.html'
    form_class = PostForm
    success_url = reverse_lazy('AdminPostBlogList')


class AdminPostBlogList(ListView):
    model = PostModel
    template_name = 'blog/postagem/admin-lista.html'


class PostUpdate(UpdateView):
    model = PostModel
    template_name = 'blog/postagem/editar.html'
    form_class = PostForm
    success_url = reverse_lazy('AdminPostBlogList')


class PostDelete(DeleteView):
    model = PostModel
    template_name = 'blog/postagem/deletar.html'
    form_class = PostForm
    success_url = reverse_lazy('AdminPostBlogList')
