from django.db import models

class Cliente(models.Model):

    FundIn = 'FI'
    FundCom = 'FC'
    MedioIn = 'MI'
    MedioCom = 'MC'
    Sup = 'SUP'

    escolaridades = [(FundIn, 'Ensino Fundamental Incompleto'),
        (FundCom, 'Ensino Fundamental Completo'),
        (MedioIn, 'Ensino Medio Incompleto'),
        (MedioCom, 'Ensino Medio Completo'),
        (Sup, 'Ensino Superior Completo')
    ]

    nome = models.CharField('Nome do Usuário', max_length=120, blank=False)
    idade = models.IntegerField(blank=False)
    email = models.EmailField('Email', max_length=254, blank=False)
    genero = models.CharField('Gênero', max_length=120, blank=False)
    escolaridade = models.CharField('Escolaridade', choices=escolaridades, max_length=2)
    curso = models.CharField('Curso', max_length=120, blank=False)
    nacionalidade = models.CharField('Nacionalidade', max_length=120, blank=False)
    # perfil_especifico = PerfilGeral.definir_perfil(self)

class PerfilGeral(models.Model):

    nome = models.CharField('Nome do Perfil', max_length=120, blank=False)
    numero_de_usuarios = models.PositiveIntegerField(blank=False, default=0)
    # perguntas = perguntas  #Quais perguntas os advogados velhos respondem

    @staticmethod
    def definir_perfil(usuario):
        # if
        #     id = 1
        # elif
        #     id = 2
        # elif
        #     id = 3
        # elif
        #     id = 4
        # elif
        #     id = 5
            
        return usuario.idade

# class Formulario(models.Model):


# class Pergunta(models.Model):


# class Resposta(models.Model):