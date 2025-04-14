from django import forms
from . models import Usuarios


class Usuarios_form(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nomes', 'bandas', 'filmes']
        labels = {'bandas': 'Banda favorita', 'filmes': 'Filme favorito' }
  