from django.db import models
from django.contrib.auth.models import User

class Pergunta(models.Model):
    nome = models.CharField('Nome da pergunta', max_length=120, blank=False)
    pergunta = models.CharField('Pergunta', max_length=120, blank=False)

    def __str__(self):
        return self.nome

class Formulario(models.Model):

    nome = models.CharField('Nome do formulário', max_length=120, blank=False)
    descricao = models.CharField('Descricao', max_length=120, blank=True, null=True)
    data_inicial = models.DateField('Data de Início', auto_now=False, auto_now_add=False, null=True)
    data_final = models.DateField('Data Final', auto_now=False, auto_now_add=False, null=True)
    perguntas = models.ManyToManyField(Pergunta, blank=True)

    def __str__(self):
        return self.nome


class PerfilGeral(models.Model):

    nome = models.CharField('Nome do Perfil', max_length=120, blank=False)
    numero_de_usuarios = models.PositiveIntegerField(blank=False, default=0)
    formularios = models.ManyToManyField(Formulario, blank=True)

    def __str__(self):
        return self.nome

class Alternativa(models.Model):
    texto = models.CharField('Texto da alternativa', max_length=120, blank=False, null=True)
    
    # cada alternativa está ligada a apenas uma pergunta
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    # Dados: quantas vezes escolhida, tempo médio de tempo de respota, etc...

    def __str__(self):
        return self.texto


class Usuario(models.Model):

    escolaridades = [('FI',   'Ensino Fundamental Incompleto'),
                     ('FC',   'Ensino Fundamental Completo'),
                     ('MI',   'Ensino Medio Incompleto'),
                     ('MC',   'Ensino Medio Completo'),
                     ('SI',  'Ensino Superior Incompleto'),
                     ('SC',  'Ensino Superior Completo')
    ]
    generos = [('Masc', 'Masculino'), ('Femin', 'Feminino'), ('Outro', 'Outro')]

    nome = models.CharField('Nome do Usuário', max_length=120, blank=False, null=True)
    email = models.EmailField('Email',blank=False,null=True,unique=True)
    idade = models.IntegerField(blank=False, null=True)
    genero = models.CharField('Gênero', blank=False,max_length=15, choices=generos, null=True)
    escolaridade = models.CharField('Escolaridade', choices=escolaridades, max_length=3, blank=False, null=True)
    curso = models.CharField('Curso', max_length=120, blank=False, null=True)
    nacionalidade = models.CharField('Nacionalidade', max_length=120, blank=False, null=True)

    # formulários respondidos
    formularios = models.ManyToManyField(Formulario, blank=True)

    # formulário que está sendo respondio
    form_atual = models.ForeignKey(Formulario, blank=True, null=True, on_delete=models.CASCADE, related_name='form_atual')
    
    # set de alternativas para o formulario que está sendo respondido, só dará certo se cada alternativa pertencer a apenas uma pergunta,
    # pois assim será possivel encontra a pergunta a partir da alternativa
    alternativas = models.ManyToManyField(Alternativa, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    perfil_especifico = models.ForeignKey(PerfilGeral, on_delete=models.DO_NOTHING, max_length=120, null=True, editable=False)


    def __str__(self):
        return self.nome

    

class Resposta(models.Model):
    pub_data = models.DateField('Data da resposta', null = True, blank = True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null = True)
    formulario = models.ForeignKey(Formulario, on_delete=models.DO_NOTHING, null = True)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.DO_NOTHING, null=True)
    alternativa = models.ForeignKey(Alternativa, on_delete=models.DO_NOTHING, null = True)

    def __str__(self):
        return self.usuario.nome + ': ' + self.pergunta.nome

# considerar perguntas com 4 alternativas e formulários com 12 perguntas (exemplo)
