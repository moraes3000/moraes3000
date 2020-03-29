from django.db import models
from blog.models.categoria import CategoriaBlogModel
from django.contrib.auth.models import User
from django.utils import timezone
# otimizar o tamanho da imagem
from PIL import Image
from django.conf import settings
import os


class PostModel(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Titulo')
    slug = models.SlugField(blank=True)
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_post = models.DateTimeField(default=timezone.now)
    conteudo_post = models.TextField(verbose_name='Conteúdo')
    excerto_post = models.TextField(verbose_name='Excerto', blank=True)
    categoria_post = models.ForeignKey(CategoriaBlogModel, on_delete=models.DO_NOTHING, blank=True, null=True,
                                       verbose_name='Categoria da postagem')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True)
    publicado_post = models.BooleanField(default=False)

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.titulo_post)

    def __str__(self):
        return self.titulo_post

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.resize_image(self.imagem_post.name, 800)
    #
    # @staticmethod
    # def resize_image(img_name, new_width):
    #     img_path = os.path.join(settings.MEDIA_ROOT, img_name)
    #     img = Image.open(img_path)
    #     width, height = img.size
    #     new_height = round((new_width * height) / width)
    #
    #     if width <= new_width:
    #         img.close()
    #         return
    #
    #     new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
    #     new_img.save(
    #         img_path,
    #         optimize=True,
    #         quality=60
    #     )
    #     new_img.close()
