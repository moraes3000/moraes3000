from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from game.forms import JogoForm

from game.models import JogoModel


# Create your views here.

class JogoListView(ListView):
    model = JogoModel
    template_name = 'game/jogo/lista.html'


class JogoCreateView(CreateView):
    model = JogoModel
    form_class = JogoForm
    template_name = 'game/jogo/adicionar.html'
    success_url = reverse_lazy('AdminJogoList')


class AdminJogoList(ListView):
    model = JogoModel
    template_name = 'game/jogo/admin-lista.html'


class JogoUpdate(UpdateView):
    model = JogoModel
    form_class = JogoForm
    template_name = 'game/jogo/adicionar.html'
    success_url = reverse_lazy('AdminJogoList')


class JogoDelete(DeleteView):
    model = JogoModel
    form_class = JogoForm
    template_name = 'game/jogo/excluir.html'
    success_url = reverse_lazy('AdminJogoList')
