from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AdminDashboardView(TemplateView):
    template_name = 'painel_de_controle/adminDashbord.html'