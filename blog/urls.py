from django.urls import path
from blog.views.blog import PostIndex, PostDetalhes
from blog.views.categoria import AdminCategoriaCreate, AdminCategoriaBlogList, AdminCategoriaUpdate, \
    AdminCategoriaDelete

urlpatterns = [
    path('', PostIndex.as_view(), name='HomeTemplateView'),
    path('lista-de-capitulos/<int:pk>/', PostDetalhes.as_view(), name='PostDetalhes'),

    # categoria
    path('admin-add-categoria-blog', AdminCategoriaCreate.as_view(), name='AdminCategoriaCreate'),
    path('admin-list-categoria-blog', AdminCategoriaBlogList.as_view(), name='AdminCategoriaBlogList'),

    path('admin-update-categoria-blog/<slug:slug>', AdminCategoriaUpdate.as_view(), name='AdminCategoriaUpdate'),
    path('admin-add-categoria-blog/<slug:slug>', AdminCategoriaDelete.as_view(), name='AdminCategoriaDelete'),

    # create - admin-add-categoria-blog

    # list - admin-list-categoria-blog
    # update - admin-update-categoria-blog
    # delete - admin-add-categoria-blog

    # postagem

    # comentario

]
