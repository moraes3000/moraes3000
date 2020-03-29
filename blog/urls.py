from django.urls import path
from blog.views.blog import PostIndex,PostDetalhes

urlpatterns = [
    path('', PostIndex.as_view(), name='HomeTemplateView'),
    path('lista-de-capitulos/<int:pk>/', PostDetalhes.as_view(), name='PostDetalhes'),

    

]
