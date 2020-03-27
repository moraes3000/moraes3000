from django.urls import reverse

from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class JogoModel(models.Model):
    nome = models.CharField(_("nome"), max_length=150)
    slug = models.SlugField(_("slug"), blank=True)
    descricao = RichTextUploadingField(u'Conteúdo', default='', blank=True, null=True)
    imagem = models.ImageField('Foto', upload_to="foto/jogo", default='', blank=True, null=True)
    criado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'

    def publish(self):
        self.criado = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('AdminJogoListView')

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome)

@receiver(pre_save, sender=JogoModel)
def nome_slug(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()


class CapituloJogoModel(models.Model):
    nome = models.CharField(_("nome"), max_length=150)
    slug = models.SlugField(_("slug"), blank=True)
    descricao = RichTextUploadingField(u'Conteúdo', default='', blank=True, null=True)
    imagem = models.ImageField('Foto', upload_to="foto/capitulo", default='', blank=True, null=True)
    criado = models.DateTimeField(default=timezone.now)
    jogo = models.ForeignKey("JogoModel", verbose_name=_("jogo"), on_delete=models.CASCADE)
    iframe = models.CharField('Apenas a Url do youtube', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Capítulo Jogo'
        verbose_name_plural = 'Capitulos dos jogos'
        ordering = ['nome']

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome)


    def get_absolute_url(self):
        return reverse('TodosCapitulosListView')

@receiver(pre_save, sender=CapituloJogoModel)
def my_handler(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()