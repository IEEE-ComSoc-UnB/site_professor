from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Usuario, PerfilGeral, Formulario, Pergunta, Alternativa, Resposta

def about(request):
	return render(request, 'blog/about_us.html')

def contact(request):
    return render(request, 'blog/contact.html')

def home(request):
    return render(request, 'blog/home.html')

def forms(request):
    forms_available = Formulario.objects.order_by('-data_inicial')
    context = {'forms_available' : forms_available}
    return render(request, 'blog/forms.html', context)

def formulario(request, form_id):
    try:
        formulario = Formulario.objects.get(pk=form_id)
    except Formulario.DoesNotExist:
        raise Http404("Formulário inexistente")
    return render(request, 'blog/formulario.html', {'formulario' : formulario})