from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from blog.models import Usuario

class ResgistroDeUsuario(UserCreationForm):
    # Herda do formulário de registro padrão do django
    class Meta:
        # define o model com o qual esse formulário irá interagir e os seus fields
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RegistroDePerfil(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','idade','genero','escolaridade','curso','nacionalidade']