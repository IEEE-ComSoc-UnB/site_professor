from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.views import LoginView,LogoutView # Views de Login e Logout
from django.contrib.auth.decorators import login_required # Limita o acesso de uma url apenas para usuários logados

from blog.models import Usuario
from django.contrib.auth.models import User

from django.contrib import messages # flashmessages

from .forms import ResgistroDeUsuario, RegistroDePerfil


def register(request):

    # Se dados forem passados via POST
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        user_form = ResgistroDeUsuario(request.POST)
        usuario_form = RegistroDePerfil(request.POST)
        
        if user_form.is_valid() and usuario_form.is_valid(): # se o formulario for valido

            username = user_form.cleaned_data.get('username') # para utilizar na flashmessage que indica que o usuário foi cadastrado
            messages.success(request, f'Conta criada para {username}!')

            u = user_form.save() # cria um novo user a partir dos dados enviados
            p = usuario_form.save() # cria um novo usuario
            p.user = u # liga o user recem criado ao usuario
            p.save()

            return redirect("/account/login/") # redireciona para a tela de login
        else:
            context = {
                'u_form': user_form,
                'p_form': usuario_form,
            }
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "account/register.html", context)
    else:
        user_form = ResgistroDeUsuario()
        usuario_form = RegistroDePerfil()
        context = {
            'u_form': user_form,
            'p_form': usuario_form,
        }
        # se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
        return render(request, "account/register.html", context)


def perfilForm(request):
    user_form = ResgistroDeUsuario(instance=request.user)
    perfil_form = RegistroDePerfil(instance=request.user.Usuario)
    
    context = {
        'u_form': user_form,
        'p_form': perfil_form,
    }
    return render(request, 'account/perfilForm.html', context)

