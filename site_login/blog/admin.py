from django.contrib import admin
from .models import Usuario, PerfilGeral, Formulario, Resposta, Pergunta, Alternativa

admin.site.site_header = "Pratica de Lembrar"
admin.site.site_title = "Área de Administração"
admin.site.index_title = "Bem vindo à Administração do site Prática de Lembrar"

# Register your models here.

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 2

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['nome']}),
                ('Pergunta', {'fields': ['pergunta']}),]

    inlines = [AlternativaInline]


admin.site.register(Usuario)
admin.site.register(PerfilGeral)
admin.site.register(Formulario)
# admin.site.register(Resposta)
admin.site.register(Pergunta, PerguntaAdmin)
# admin.site.register(Alternativa)