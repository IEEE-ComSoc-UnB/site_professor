from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'account'

urlpatterns = [
    path('registrar/', views.register, name='register'),

    # mudar a variável template_name de LoginView de registration/login.html para account/login.html
    path('login/', LoginView.as_view(template_name="account/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/form', views.perfilForm, name='perfilForm')
]
