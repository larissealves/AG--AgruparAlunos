from django.contrib import admin
from .models import Grupo, Aluno

#admin.site.register(Grupo)
#admin.site.register(Aluno)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome_aluno", "caracteristica_aluno")
    
@admin.register(Grupo)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome_grupo", "caracteristica_grupo", "limite_integrante_grupo")
    change_list_template = 'agrupar_alunos/link.html'

