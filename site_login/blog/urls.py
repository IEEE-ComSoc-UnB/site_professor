from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre-nos/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
    path('form/', views.form, name='form')
]