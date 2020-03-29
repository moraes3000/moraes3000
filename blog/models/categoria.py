from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.
class CategoriaBlogModel(models.Model):
    nome_cat = models.CharField(max_length=255)
    slug = models.SlugField(_("slug"), blank=True)

    class Meta:
        verbose_name = 'Categoria Blog'
        verbose_name_plural = 'Categorias Blog'
        ordering = ['nome_cat']

    def __str__(self):
        return self.nome_cat

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome_cat)


@receiver(pre_save, sender=CategoriaBlogModel)
def nome_slug(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()
