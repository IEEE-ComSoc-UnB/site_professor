from django.db import models

class PerfilGeral(models.Model):

    nome = models.CharField('Nome do Perfil', max_length=120, blank=False)
    numero_de_usuarios = models.PositiveIntegerField(blank=False, default=0)

    def __str__(self):
        return self.nome


class Cliente(models.Model):

    FundIn = 'FI'
    FundCom = 'FC'
    MedioIn = 'MI'
    MedioCom = 'MC'
    Sup = 'SUP'
    Masc = 'M'
    Femin = 'F'
    Outro = 'O'

    escolaridades = [(FundIn, 'Ensino Fundamental Incompleto'),
        (FundCom, 'Ensino Fundamental Completo'),
        (MedioIn, 'Ensino Medio Incompleto'),
        (MedioCom, 'Ensino Medio Completo'),
        (Sup, 'Ensino Superior Completo')
    ]

    generos = [(Masc, 'Masculino'), (Femin, 'Feminino'), (Outro, 'Outro')]

    nome = models.CharField('Nome do Usuário', max_length=120, blank=False)
    idade = models.IntegerField(blank=True, null=True)
    email = models.EmailField('Email', max_length=254, blank=True, null=True)
    genero = models.CharField('Gênero', max_length=2, blank=True, choices=generos, null=True)
    escolaridade = models.CharField('Escolaridade', choices=escolaridades, max_length=3, blank=True, null=True)
    curso = models.CharField('Curso', max_length=120, blank=True, null=True)
    nacionalidade = models.CharField('Nacionalidade', max_length=120, blank=True, null=True)

    def definir_perfil(nome, idade, email, genero, escolaridade, curso, nacionalidade):
        if nome == 'kfouri':
            return 1
        return nome

    # perfil_especifico = models.ForeignKey(editable=False, default=definir_perfil(nome, idade, email, genero, escolaridade, curso, nacionalidade), max_length=120)

    def __str__(self):
        return self.nome

class Formulario(models.Model):

    nome = models.CharField('Nome do Formulário', max_length=120, blank=False)
    descricao = models.CharField('Descricao', max_length=120, blank=True, null=True)
    data_inicial = models.DateField('Data de Início', auto_now=False, auto_now_add=False, null=True)
    data_inicial = models.DateField('Data de Início', auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.nome

class Resposta(models.Model):

    nome = models.CharField('Nome da Resposta', max_length=120, blank=False)

    def __str__(self):
        return self.nome


class Pergunta(models.Model):

    nome = models.CharField('Nome da Pergunta', max_length=120, blank=False)
    pergunta = models.CharField('Pergunta', max_length=120, blank=False)
    key = models.ForeignKey(Formulario, on_delete=models.DO_NOTHING)
    key2 = models.ForeignKey(Resposta, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.nome

