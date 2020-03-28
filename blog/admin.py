from django.contrib import admin
# Register your models here.
from blog.models.categoria import CategoriaBlogModel
from blog.models.post import PostModel
from blog.models.comentario import ComentarioModel

class CategoriaBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cat')



class PostAdmin(admin.ModelAdmin):
    list_display = ('id','titulo_post', 'autor_post', 'data_post','categoria_post', 'publicado_post')

    list_editable = ('publicado_post',)
    list_display_links = ('id', 'titulo_post',)


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id','nome_comentario', 'email_comentario','post_comentario','data_comentario', 'publicado_comentario')
    list_editable = ('publicado_comentario',)
    list_display_links = ('id', 'nome_comentario', 'email_comentario')






admin.site.register(CategoriaBlogModel, CategoriaBlogAdmin)
admin.site.register(PostModel, PostAdmin)
admin.site.register(ComentarioModel, ComentarioAdmin)