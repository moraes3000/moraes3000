from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.urls import reverse_lazy
from  game.forms import JogoForm

from game.models import JogoModel
# Create your views here.

class JogoListView(ListView):
    model = JogoModel
    template_name = 'jogo/lista.html'


class JogoCreateView(CreateView):
    model = JogoModel
    form_class = JogoForm
    template_name = 'jogo/adicionar.html'

    success_url = reverse_lazy()

class AdminJogoList(ListView):
    model = JogoModel
    template_name = 'jogo/admin-lista.html'

