from django.urls import path
from .views import JogoListView, CapituloJogoListView,CapituloJogoDetailView

urlpatterns = [
    path('', JogoListView.as_view(), name='JogoListView'),
    path('lista-de-capitulos/<int:pk>/', CapituloJogoListView.as_view(), name='CapituloJogoListView'),
    path('capitulo/<slug:slug>/', CapituloJogoDetailView.as_view(), name='CapituloJogoDetailView'),

]
