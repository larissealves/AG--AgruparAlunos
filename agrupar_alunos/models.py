from django.db import models

class Grupo(models.Model):
    nome_grupo = models.CharField(max_length=200, verbose_name = "Grupo", blank = False)
    caracteristica_grupo = models.CharField(max_length=200, verbose_name = "Característica Grupo", blank = False)
    limite_integrante_grupo = models.IntegerField(verbose_name = "Limite de Integrantes", blank = False)
   
    def __str__(self):
        return self.nome_grupo

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=200, verbose_name = "Aluno", blank = False)
    caracteristica_aluno = models.CharField(max_length=200, verbose_name = "Característica Aluno", blank = False)
   
    def __str__(self):
        return self.nome_aluno 


