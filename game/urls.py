from django.urls import path
from game.views.capitulos import CapituloJogoListView, CapituloJogoDetailView, AdminCapituloList, CapituloCreate, \
    CapituloUpdate, CapituloDelete
from game.views.jogos import JogoListView, JogoCreateView, AdminJogoList, JogoUpdate, JogoDelete

urlpatterns = [
    path('', JogoListView.as_view(), name='JogoListView'),
    # admin
    path('admin-add-jogo', JogoCreateView.as_view(), name='JogoCreateView'),
    path('admin-listar-jogo', AdminJogoList.as_view(), name='AdminJogoList'),
    path('admin-editar-jogo/<slug:slug>',JogoUpdate.as_view(), name='JogoUpdate'),
    path('admin-remover-jogo/<slug:slug>', JogoDelete.as_view(), name='JogoDelete'),

    # Capitulos
    path('lista-de-capitulos/<int:pk>/', CapituloJogoListView.as_view(), name='CapituloJogoListView'),
    path('capitulo/<slug:slug>/', CapituloJogoDetailView.as_view(), name='CapituloJogoDetailView'),
    #admin
    path('admin-listar-capitulo', AdminCapituloList.as_view(), name='AdminCapituloList'),
    path('admin-add-capitulo', CapituloCreate.as_view(), name='CapituloCreate'),
    path('admin-editar-capitulo/<slug:slug>', CapituloUpdate.as_view(), name='CapituloUpdate'),
    path('admin-remover-capitulo/<slug:slug>', CapituloDelete.as_view(), name='CapituloDelete'),

]
