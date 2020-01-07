from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.views import LoginView,LogoutView # Views de Login e Logout
from django.contrib.auth.decorators import login_required # Limita o acesso de uma url apenas para usuários logados
from blog.views import home

from django.contrib import messages # flashmessages

from .forms import ResgistroDeUsuario, RegistroDePerfil


def register(request):
    # Se dados forem passados via POST
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = ResgistroDeUsuario(request.POST)

        if form.is_valid(): # se o formulario for valido

            username = form.cleaned_data.get('username') # para utilizar na flashmessage que indica que o usuário foi cadastrado
            messages.success(request, f'Conta criada para {username}!')

            form.save() # cria um novo usuario a partir dos dados enviados
 
            return redirect("/account/login/") # redireciona para a tela de login
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "account/register.html", {"form": form})
    
    # se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
    return render(request, "account/register.html", {"form": ResgistroDeUsuario()})

def perfilForm(request):
    usuario_form = ResgistroDeUsuario()
    perfil_form = RegistroDePerfil()
    
    context = {
        'u_form': usuario_form,
        'p_form': perfil_form,
    }
    return render(request, 'account/perfilForm.html', context)