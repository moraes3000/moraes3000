from django.forms.models import ModelForm
from blog.models.post import PostModel
from blog.models.categoria import CategoriaBlogModel
from blog.models.comentario import ComentarioModel
from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('titulo_post', 'autor_post','conteudo_post','categoria_post','imagem_post','publicado_post')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn-success'))
        self.helper.add_input(Button('cancel', "Cancelar", css_class='btn-danger', onclick="javascript:history.back()"))


class CategoriaBlogForm(forms.ModelForm):
    class Meta:
        model = CategoriaBlogModel
        fields = ('nome_cat',)

    def __init__(self, *args, **kwargs):
        super(CategoriaBlogForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn-success'))
        self.helper.add_input(Button('cancel', "Cancelar", css_class='btn-danger', onclick="javascript:history.back()"))


class ComentarioBlogForm(forms.ModelForm):

    def clean(self):
        data = self.cleaned_data
        # print(data)
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('nome_comentario_comentario')

        if len(nome) < 3:
            self.add_error(
                'nome_comentario',
                'Nome precisar ter mais de 3 caracteres'

            )
        if len(comentario) < 3:
            self.add_error(
                'nome_comentario_comentario',
                'Nome precisar ter mais de 3 caracteres'

            )

    class Meta:
        model = ComentarioModel
        fields = ('nome_comentario', 'email_comentario', 'nome_comentario_comentario')

    def __init__(self, *args, **kwargs):
        super(ComentarioBlogForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn-success'))
        self.helper.add_input(
            Button('cancel', "Cancelar", css_class='btn-danger', onclick="javascript:history.back()"))
