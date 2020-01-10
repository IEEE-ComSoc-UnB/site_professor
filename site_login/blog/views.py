from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Usuario, PerfilGeral, Formulario, Pergunta, Alternativa, Resposta

from django.contrib.auth.decorators import login_required # Limita o acesso de uma url apenas para usuários logados

def about(request):
	return render(request, 'blog/about_us.html')

def contact(request):
    return render(request, 'blog/contact.html')

def home(request):
    return render(request, 'blog/home.html')


@login_required
def forms(request):
    usuario_logado = request.user                                   #user logado
    usuario_logado = usuario_logado.usuario                         #usuario logado
    perfil = usuario_logado.perfil_especifico                       #perfil do usuario logado
    forms_available = perfil.formularios.order_by('-data_inicial')  #formularios do perfil
    context = {'forms_available' : forms_available}
    return render(request, 'blog/forms.html', context)


@login_required
def formulario(request, form_id):
    try:
        formulario = Formulario.objects.get(pk=form_id)
    except Formulario.DoesNotExist:
        raise Http404("Formulário inexistente")
    return render(request, 'blog/formulario.html', {'formulario' : formulario})