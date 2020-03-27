from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.urls import reverse_lazy

from game.models import JogoModel, CapituloJogoModel

class CapituloJogoListView(ListView):
    model = CapituloJogoModel
    template_name = 'capitulo/lista.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        capitulo = CapituloJogoModel.objects.filter(jogo=pk)
        return capitulo

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pk = self.kwargs.get('pk')
        context['object'] = JogoModel.objects.get(pk=pk)
        return context



class CapituloJogoDetailView(DetailView):
    model = CapituloJogoModel
    template_name = 'capitulo/detalhe.html'
