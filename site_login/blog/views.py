from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Usuario, PerfilGeral, Formulario, Pergunta, Alternativa, Resposta
from django.utils import timezone

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
    forms_disponiveis = perfil.formularios.order_by('-data_inicial')  #formularios do perfil
    forms_respondidos = usuario_logado.formularios.all()

    # se todos os formulários foram respondidos
    if len(forms_disponiveis) == len(forms_respondidos):
        
        # pag_anterior = request.META.HTTP_REFERER
        # context = {
        #     'pag_anterior': pag_anterior
        # }
        return render(request, 'blog/forms_respondidos.html', {})
    elif len(forms_disponiveis) < len(forms_respondidos):
        return HttpResponse('<h1 style="color:red">ERRO: Mais formulários respondidos do que disponíveis<h1>')


    context = {
    'forms_disponiveis' : forms_disponiveis,
    'forms_respondidos' : forms_respondidos
    }
    return render(request, 'blog/forms.html', context)


@login_required
def formulario(request, form_id):
    try:
        formulario = Formulario.objects.get(pk=form_id)
    except Formulario.DoesNotExist:
        raise Http404("Formulário inexistente")
    return render(request, 'blog/formulario.html', {'formulario' : formulario})


@login_required
def pergunta(request, form_id, pergunta_num):

    formulario = Formulario.objects.get(pk=form_id)
    if pergunta_num == len(formulario.perguntas.all()):
        request.user.usuario.formularios.add(formulario)
        return redirect('/formulario')   #tela de formulario terminado 


    try:
        pergunta = formulario.perguntas.all()[pergunta_num]
        context = {
            'formulario': formulario,
            'pergunta': pergunta,
            'pergunta_num': pergunta_num
        }
    except IndexError:
        # pergunta fora do formulario
        return redirect('/error')
 
        
    return render(request, 'blog/pergunta.html', context)


@login_required
def voltar(request, form_id, pergunta_num):

    formulario = Formulario.objects.get(pk=form_id)
    pergunta_num -= 1
    try:
        pergunta = formulario.perguntas.all()[pergunta_num]
        context = {
            'formulario': formulario,
            'pergunta': pergunta,
            'pergunta_num': pergunta_num
        }
    except IndexError:
        # pergunta fora do formulario
        return redirect('/error')
 
        
    return render(request, 'blog/pergunta.html', context)


@login_required
def resposta(request, form_id, pergunta_num):

    pub_data    = timezone.now().date()

    usuario     = request.user.usuario
    formulario  = get_object_or_404(Formulario, pk=form_id)
    pergunta    = formulario.perguntas.all()[pergunta_num]

    try:
        alternativa_id = request.POST['alternativa']
    except (KeyError, Alternativa.DoesNotExist):
        return render(request, 'blog/pergunta.html', {
            'formulario': formulario,
            'pergunta': pergunta,
            'pergunta_num': pergunta_num,
            'error_message': "Você não escolheu uma alternativa."
        })
    alternativa = Alternativa.objects.get(pk=alternativa_id)

    Resposta.objects.create(pub_data=pub_data, usuario=usuario, formulario=formulario, pergunta=pergunta, alternativa=alternativa)
    pergunta_num += 1
    url = '/formulario/' + str(form_id) +'/pergunta/' + str(pergunta_num)
    return redirect(url)


def formConcluido(request):
    
    forms_respondidos = len(request.user.usuario.formularios.all())
    
    context = {
        'forms_repondidos': forms_respondidos
    }
    return render(request, 'blog/form_concluido.html', context)

