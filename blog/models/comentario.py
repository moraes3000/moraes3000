from django.db import models
from blog.models.post import PostModel
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class ComentarioModel(models.Model):
    nome_comentario = models.CharField(max_length=255)
    email_comentario = models.EmailField()
    nome_comentario_comentario = models.TextField()
    post_comentario = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_comentario


    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
