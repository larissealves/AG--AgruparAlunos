from django.shortcuts import render
from .models import Grupo, Aluno
from random import random
from django.views.generic import TemplateView, FormView, ListView

individou_ja_escolhidos = 0
resul = []
'''
def HomePageView(request):
    #Mudar nome da função : Salvar caracteristicas e nome dos alunos em um lista. Assim como, o script

    alunos = Aluno.objects.all()
    nome_a = []
    caracteristicas_a = []

    for aluno in alunos:
        alunos_nome = aluno.nome_aluno
        alunos_caractteristicas = aluno.caracteristica_aluno

        nome_a.append(alunos_nome)
        caracteristicas_a.append(aluno.caracteristica_aluno)

    context = {'alunos_nome':nome, 'alunos_caracteristicas': caracteristicas}
'''


class Produto():
    def __init__(self, nome, caracteristica):
        self.nome = nome
        self.caracteristica = caracteristica
        
class Grupoo():
    def __init__(self, caracteristicas_grupo, numero_integrantes_grupo):
        self.caracteristicas_grupo = caracteristicas_grupo
        self.numero_integrantes_grupo = numero_integrantes_grupo
        self.grupo = []
              
        
class Individuo():
    def __init__(self, nome, caracteristicas, limite_integrante_grupo, grupo, geracao=0): 
        self.caracteristicas = caracteristicas
        self.nome = nome
        #self.valores = valores
        self.limite_integrante_grupo = limite_integrante_grupo
        self.alunos_no_grupo = 0
        self.grupo = grupo
        self.nota_avaliacao = 0
        self.geracao = geracao

        self.cromossomo = []

        #print('\nr', resul)


        #a = 0
        #cont = 0
        #print(novo_individuo)
        
        '''
        for i in range(len(caracteristicas)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
        
            if self.cromossomo[i] == '1':
                a +=1
                    
                if a > self.limite_integrante_grupo:
                    if self.cromossomo[i] == '1':
                        self.cromossomo[i] = '0'

                    if a < self.limite_integrante_grupo:
                        if self.cromossomo[i] == '0':
                            self.cromossomo[i] = '1'
        '''
        cont = 0
       
       
        #self.cromossomo = []
        if (len(resul)) == 0:

            for i in range(len(caracteristicas)):
                
                    if random() < 0.6:
                        self.cromossomo.append("0")
                    else:
                        if cont < self.limite_integrante_grupo:
                            self.cromossomo.append("1")                     
                            cont += 1
                        else:
                            self.cromossomo.append("0")
        else:
            qunt_int_grupo = 0
            quant_cromo_n_selecionados = 0
            novo_cromo = []

            for r in range(len(resul)):
                if resul[r] == '0':
                    quant_cromo_n_selecionados += 1
                    if qunt_int_grupo < self.limite_integrante_grupo and quant_cromo_n_selecionados > 0:
                        self.cromossomo.append('1')
                        qunt_int_grupo += 1
                    else:
                        self.cromossomo.append('0')

                if resul[r] == '1':
                    self.cromossomo.append('0')
        '''
        for r in range(len(resul)):
                if resul[r] == '0':
                    quant_cromo_n_selecionados += 1
                    if random() < 0.6:
                        self.cromossomo.append('0')
                    else:
                        if quant_cromo_n_selecionados >= 0 and qunt_int_grupo < self.limite_integrante_grupo:
                            self.cromossomo.append('1')
                            qunt_int_grupo += 1
                        else:
                            self.cromossomo.append('0')    
                if resul[r] == '1':
                    self.cromossomo.append('0')
        '''



        '''
        for i in novo_individuo:
            for n in self.cromossomo:

                #alterar_tipo = str(self.cromossomo[i])
                if i == n:
                    print('iguais')
        '''
        '''
        print('\nc', self.cromossomo)  
        intgrantes_grupo = 0
        for c in novo_individuo:
            
            for n in self.cromossomo:
                itera = 0
                print('posicao a', self.cromossomo.index(n) )
                if c == '0'  and n == '1':
                    pass
                if c == '1'  and n == '1':
                    itera += 1
                   
                    altera_bit = round(random()  * len(self.cromossomo))
                    self.cromossomo[i] = '0'
   
                    
                    
                    for n in range (len(self.cromossomo)):
                        if self.cromossomo[i] ==1:
                            intgrantes_grupo += 1
                        if n == altera_bit:
                            if intgrantes_grupo < self.limite_integrante_grupo:
                                self.cromossomo[i] = '1'                     
                                intgrantes_grupo += 1
                            
                                

                        
                else:
                    pass
        print('\nz', self.cromossomo)
        ''' 
      
#AVALIAR
    def avaliacao(self):
        
        quantidade_cromossomos_1 = 0        
        soma_espaco_disponivel = 0
        nota_por_aluno = 0

        
        for g in range(len(caracteristicas_grupo)):
            
            for i in range(len(caracteristicas)):
                 
                if(self.cromossomo[i]=='1'):
                    if self.caracteristicas[i] == caracteristicas_grupo[g]:
                        nota_por_aluno = self.caracteristicas[i].count(caracteristicas_grupo[g] )+ 0.35
                    else:
                        nota_por_aluno = 1 + 0.35

               
            self.nota_avaliacao += nota_por_aluno 
            #print(self.nota_avaliacao)
                    #self.alunos_no_grupo = self.limite_integrante_grupo - quantidade_cromossomos_1 #diminuir espacoes disponiveis no grupo
       # print('\n', self.cromossomo, '= ', self.nota_avaliacao, '\n')
        
                  


     
    def crossover(self, outro_individuo):
        #print('\noutro', outro_individuo.cromossomo)
        #print('\ncromo 1', self.cromossomo)
        corte = round(random()  * len(self.cromossomo))
        #print('\nPonto de corte', corte)
       
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(self.nome, self.caracteristicas, self.limite_integrante_grupo, self.grupo, self.geracao + 1),
                  Individuo(self.nome, self.caracteristicas, self.limite_integrante_grupo, self.grupo, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        #print('\nFilho 1', filho1)
        #print('\nFilho 2', filho2)
        return filhos
                   
    def mutacao(self, taxa_mutacao):
        #("\nAntes %s " % self.cromossomo, '\n')
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
       # print("Depois %s " % self.cromossomo)
        return self

class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        
    def inicializa_populacao(self, nome, caracteristicas, limite_integrante_grupo, caracteristicas_grupo):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(nome, caracteristicas, limite_integrante_grupo, caracteristicas_grupo))
        self.melhor_solucao = self.populacao[0]
   
    
        
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
        
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
        
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
           soma += individuo.nota_avaliacao
        return soma
        
    def seleciona_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        return pai
    
    def visualiza_geracao(self):
        melhor = self.populacao[0]
        '''
        print("G:%s -> NOTA: %s Cromossomo: %s" % (self.populacao[0].geracao,
                                                               melhor.nota_avaliacao,
                                                               melhor.cromossomo))
        '''
        
    def resolver(self, taxa_mutacao, numero_geracoes, nome, caracteristicas, limite_integrante_grupo, caracteristicas_grupo):
        self.inicializa_populacao(nome, caracteristicas, limite_integrante_grupo, caracteristicas_grupo)
        

        for individuo in self.populacao:
            individuo.avaliacao()
        
        self.ordena_populacao()
        
        self.visualiza_geracao()
        
        for geracao in range(numero_geracoes):
            soma_avaliacao = self.soma_avaliacoes()
            nova_populacao = []
            
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.seleciona_pai(soma_avaliacao)
                pai2 = self.seleciona_pai(soma_avaliacao)
                
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
            
            self.populacao = list(nova_populacao)
            
            for individuo in self.populacao:
                individuo.avaliacao()
                
            
            self.ordena_populacao()
            
            self.visualiza_geracao()
            
            melhor = self.populacao[0]
            self.melhor_individuo(melhor)

        '''
        print("\nMelhor solução -> G: %s Nota: %s Cromossomo: %s" %
              (self.melhor_solucao.geracao,
               self.melhor_solucao.nota_avaliacao,
               self.melhor_solucao.cromossomo))
        
        print('\n')
        '''
        return self.melhor_solucao.cromossomo
        
        
alunos = Aluno.objects.all()
grupos = Grupo.objects.all()

nome = []
caracteristicas = []

for aluno in alunos:
    alunos_nome = aluno.nome_aluno
    alunos_caractteristicas = aluno.caracteristica_aluno

    nome.append(alunos_nome)
    caracteristicas.append(aluno.caracteristica_aluno)

# print('\n',nome)
# print('\n', caracteristicas, '\n')

  




lista_grupos = []
lista_grupos.append(Grupo("Grupo 01 ", 'B', 6))
lista_grupos.append(Grupo("Grupo 02 ", 'A', 3))
lista_grupos.append(Grupo("Grupo 03 ", 'C', 3))
lista_grupos.append(Grupo("Grupo 04 ", 'D', 2))

nome_grupo = []
caracteristicas_grupo = []
numero_integrantes_grupo = []

for grupo in grupos:
    nome_grupo.append(grupo.nome_grupo)
    caracteristicas_grupo.append(grupo.caracteristica_grupo)
    numero_integrantes_grupo.append(grupo.limite_integrante_grupo)

#print(nome_grupo)

'''
print('\n', caracteristicas_grupo)
print('\n', numero_integrantes_grupo, '\n')


for i in range (len(caracteristicas_grupo)):
    individuo1 = Individuo(nome, caracteristicas, numero_integrantes_grupo[i], caracteristicas_grupo[i])
    individuo1.avaliacao()   

'''
cont = 0     
tamanho_populacao = 20
taxa_mutacao = 0.01
numero_geracoes = 100

melhores_solucoes_finais = []
grupos_melhor_solucao = []
solucao_final_tempale = []

resul_momento = []

for i in range(len(nome)):
    resul_momento.append("0")

for i in range(len(caracteristicas_grupo)):
        
    ag = AlgoritmoGenetico(tamanho_populacao)
    resultado = ag.resolver(taxa_mutacao, numero_geracoes, nome, caracteristicas, numero_integrantes_grupo[i], caracteristicas_grupo[i])
    
    #print('\nCROMOSSOMO RESULTANTE: ', resultado)
    
    #print('\n')
    #print('*'*70)
    #print(nome_grupo[i], '|', 'Caracteristica', caracteristicas_grupo[i], "->", " QNT Integrantes:", numero_integrantes_grupo[i], "       ")
    
    caract_grupo = caracteristicas_grupo[i]
    quantidade_integrantes = numero_integrantes_grupo[i]
    #print('-'*70)
    #nova_lista_nome = []
    novo_individuo = list(resultado)
    for i in range(len(nome)):
        
        if resultado[i] == '1' and nome[i]:
            
            melhores_solucoes_finais.append(nome[i]) 
            resul_momento[i] = '1'
            resul = resul_momento
            print('\n\n\n')
            #tam =  len(melhores_solucoes_finais)
           
            #for i in range (tam):

            
            #nova_lista_nome = nome.copy()
              
            
                   
            #print('b', nova_lista_nome)
            '''
            a = nome[i]
            b = nome.index(a)
            nova_lista_nome = nome.copy()        
            nova_lista_nome .pop(b)
            
            print('a', nova_lista_nome) 
            '''


    solucao_final = caract_grupo, quantidade_integrantes,  melhores_solucoes_finais
    solucao_final_tempale.append(solucao_final)
    #print('\n')
    #print(solucao_final)
    
    #print('solucao_final_tempale', solucao_final_tempale)

    #solucao_final = caract_grupo, quantidade_integrantes,  melhores_solucoes_finais
    #solucao_final_tempale.append(solucao_final)

    #print('aaaa', g)
               
        
             
    #print('\nTODAS INFOS: ', 'GRUPO: ', caract_grupo, 'LIMITE: ', quantidade_integrantes, 'INTEGRANTES: ', melhores_solucoes, '\n' )
    #print('\n\n', melhores_solucoes_finais)
    #nome =  list(nova_lista_nome)
    melhores_solucoes_finais = []


print("\n")
def resultados(request):
           
    return render(request, 'agrupar_alunos/home.html', {'caract_grupo': solucao_final_tempale })
                 


     