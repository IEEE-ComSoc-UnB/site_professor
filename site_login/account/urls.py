from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'account'

urlpatterns = [
    path('registrar/', views.register, name='register'),

    # mudar a variável template_name de LoginView de registration/login.html para account/login.html
    path('login/', LoginView.as_view(template_name="account/login.html", redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfilVisualizar, name='perfilVisualizar'),
    path('perfil/atualizar', views.perfilAtualizar, name='perfilAtualizar')
]
