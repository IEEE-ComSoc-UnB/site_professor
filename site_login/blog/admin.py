from django.contrib import admin
from .models import Usuario, PerfilGeral, Formulario, Resposta, Pergunta, Alternativa

# Register your models here.

admin.site.register(Usuario)
admin.site.register(PerfilGeral)
admin.site.register(Formulario)
admin.site.register(Resposta)
admin.site.register(Pergunta)
admin.site.register(Alternativa)