from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from blog.forms import CategoriaBlogForm
from blog.models.categoria import CategoriaBlogModel


class AdminCategoriaCreate(CreateView):
    model = CategoriaBlogModel
    template_name = 'blog/categoria/criar.html'
    form_class = CategoriaBlogForm
    success_url = reverse_lazy('AdminCategoriaBlogList')


class AdminCategoriaBlogList(ListView):
    model = CategoriaBlogModel
    template_name = 'blog/categoria/lista.html'


class AdminCategoriaUpdate(UpdateView):
    model = CategoriaBlogModel
    template_name = 'blog/categoria/editar.html'
    form_class = CategoriaBlogForm
    success_url = reverse_lazy('AdminCategoriaBlogList')


class AdminCategoriaDelete(DeleteView):
    model = CategoriaBlogModel
    template_name = 'blog/categoria/deletar.html'
    form_class = CategoriaBlogForm
    success_url = reverse_lazy('AdminCategoriaBlogList')
