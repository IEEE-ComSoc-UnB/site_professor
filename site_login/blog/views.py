from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Usuario, PerfilGeral, Formulario, Pergunta, Alternativa, Resposta
from .models import Arvore, Question, Escolha, Raiz, Tela

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
        return render(request, 'blog/forms_respondidos.html', {})

    elif len(forms_disponiveis) < len(forms_respondidos):
        return HttpResponse('<h1 style="color:red">ERRO: Mais formulários respondidos do que disponíveis<h1>')

    if usuario_logado.form_atual:
        ultima_perg = len(usuario_logado.alternativas.all())
    else:
        ultima_perg = None

    context = {
    'forms_disponiveis' : forms_disponiveis,
    'forms_respondidos' : forms_respondidos,
    'ultima_perg' : ultima_perg
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
    usuario = request.user.usuario
    # Usuario entrando no formulário pela primeira vez
    if not usuario.form_atual and pergunta_num == 0:
        print(formulario)
        usuario.form_atual = formulario
        usuario.save()

    # terminou formulario
    if pergunta_num == len(formulario.perguntas.all()):
        for alt in usuario.alternativas.all():
            usuario.alternativas.remove(alt)
        usuario.formularios.add(formulario)
        usuario.form_atual = None
        usuario.save()
        return redirect('/formulario')   #tela de formulario terminado 


    try:
        pergunta_anterior = pergunta_num -1
        pergunta = formulario.perguntas.all()[pergunta_num]
        context = {
            'formulario': formulario,
            'pergunta': pergunta,
            'pergunta_num': pergunta_num,
            'num_de_perguntas': len(formulario.perguntas.all())
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

    # se o usuario responder uma pergunta ja respondida, essa resposta deve ser atualizada
    perguntas_respondidas = [alt.pergunta for alt in usuario.alternativas.all()]
    if pergunta in perguntas_respondidas:
        for alt in pergunta.alternativa_set.all():
            if alt in usuario.alternativas.all():
                usuario.alternativas.remove(alt)

                # apagar resposta antiga
                # encontra a resposta pela alternativa escolhida,
                #já que cada alternativa possui apenas uma pergunta
                usuario.resposta_set.filter(alternativa=alt)[0].delete()
                break
    
    usuario.alternativas.add(alternativa)

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


# ===================

def arvore(request, tela_id=None):
    if tela_id:
        tela_atual = Tela.objects.get(pk=tela_id)
    else:
        tela_atual = Raiz.objects.all()[0].tela
        
    escolhas = tela_atual.question.escolha_set.all()
    

    context= {
        'tela':tela_atual,
        'escolhas': escolhas
    }
    return render(request, 'blog/tela.html', context)

