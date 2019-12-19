from django.db import models

class Usuario(models.Model):

    def __init__(self, nome, idade, genero, escolaridade, curso, nacionalidade):
        self.idade = idade
        self.nome = nome
        self.genero = genero
        self.escolaridade = escolaridade
        self.curso = curso
        self.nacionalidade = nacionalidade
        self.perfil_especifico = PerfilGeral.definir_perfil(self)

class PerfilGeral(models.Model):

    def __init__(self, nome, perguntas):
        self.nome = nome            #Perfil dos advogados velhos
        self.numero_de_usuarios = 0 #Estatisticas começam zeradas
        self.perguntas = perguntas  #Quais perguntas os advogados velhos respondem

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

user = Usuario('guilherme', 20, 'macho', 1, 1, 1)
print(user.perfil_especifico)
