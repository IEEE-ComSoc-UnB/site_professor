from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-nos/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
    path('forms/', views.forms, name='forms'),
    path('formulario/<int:form_id>', views.formulario, name='formulario'),
    path('formulario/<int:form_id>/pergunta/<int:pergunta_num>', views.pergunta, name='pergunta'),
    path('formulario/<int:form_id>/pergunta/<int:pergunta_num>/resposta', views.resposta, name='resposta'),
    path('formulario/', views.formConcluido, name='formConcluido'),

    path('arvore/', views.arvore, name='arvore'),
    path('arvore/<int:tela_id>', views.arvore, name='arvore'),
    path('arvore/<int:arvore_id>/concluida', views.arvoreConcluida, name='arvoreConcluida'),
    
]