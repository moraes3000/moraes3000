from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
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
    success_url = reverse_lazy('AdminJogoList')

class AdminJogoList(ListView):
    model = JogoModel
    template_name = 'jogo/admin-lista.html'


class JogoUpdate(UpdateView):
    model = JogoModel
    form_class = JogoForm
    template_name = 'jogo/adicionar.html'
    success_url = reverse_lazy('AdminJogoList')

    # def get_success_url(self):
    #     return reverse('AdminJogoList', kwargs={})


class JogoDelete(DeleteView):
    model = JogoModel
    form_class = JogoForm
    template_name = 'jogo/excluir.html'
    success_url = reverse_lazy('AdminJogoList')




#
# class RequisicaoDeNumerariosDeleteView(DeleteView):
#     model = RequisicaoDeNumerariosModel
#     template_name = 'requisaodenumerarios/requisicao-de-numerarios/excluir.html'
#     success_url = reverse_lazy('formulariosbasicos:pagamento-listar')

