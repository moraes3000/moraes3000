from django.forms.models import  ModelForm
from game.models import JogoModel
from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button

class JogoForm(forms.ModelForm):
    class Meta:
        model = JogoModel
        fields = ('nome', 'descricao', 'imagem',)

    def __init__(self, *args, **kwargs):
        super(JogoForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn-success'))
        self.helper.add_input(Button('cancel', "Cancelar", css_class='btn-danger', onclick="javascript:history.back()"))