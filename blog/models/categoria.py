from django.db import models

# Create your models here.
class CategoriaBlogModel(models.Model):
    nome_cat = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_cat

    class Meta:
        verbose_name = 'Categoria Blog'
        verbose_name_plural = 'Categorias Blog'
        ordering = ['nome_cat']