from django.db import models

class Grupo(models.Model):
    nome_grupo = models.CharField(max_length=200)
    caracteristica_grupo = models.CharField(max_length=200)
    limite_integrante_grupo = models.IntegerField()
   
    def __str__(self):
        return self.nome_grupo + " - " + self.caracteristica_grupo + " - " + str(self.limite_integrante_grupo)

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=200)
    caracteristica_aluno = models.CharField(max_length=200)
   
    def __str__(self):
        return self.nome_aluno + " - " + self.caracteristica_aluno


