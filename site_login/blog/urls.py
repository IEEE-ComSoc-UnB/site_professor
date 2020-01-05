from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre-nos/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
    path('forms/', views.forms, name='forms'),
    path('formulario/<int:formulario_id>', views.formulario, name='formulario')
]