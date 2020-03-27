from django.urls import path
from painel_de_controle.views import AdminDashboardView

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='AdminDashboardView'),

]
