from django.urls import path
from blog.views.blog import PostIndex, PostDetalhes, PostDelete,PostUpdate ,AdminPostBlogList ,PostAdmin
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
    # create - admin-add-postagem-blog
    # list - admin-list-postagem-blog
    # update - admin-update-postagem-blog
    # delete - admin-add-postagem-blog
    # postagem
    path('admin-add-postagem-blog', PostAdmin.as_view(), name='PostAdmin'),
    path('admin-list-postagem-blog', AdminPostBlogList.as_view(), name='AdminPostBlogList'),
    path('admin-update-postagem-blog/<slug:slug>', PostUpdate.as_view(), name='PostUpdate'),
    path('admin-add-postagem-blog/<slug:slug>', PostDelete.as_view(), name='PostDelete'),

    # comentario

]
