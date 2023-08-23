import random

def diagonal(m):
    for i in range(len(m)):
        for j in range(i):
            m[i][j] = 1
    return m

def mostra_matriz(m):
    for i in range(len(m)):
        print(m[i])
def cria_matriz(l, c):
    matriz = []
    for i in range(l):
        matriz.append([])
        for j in range(c):
            matriz[i].append(random.randint(0,10))
    return matriz
def altera_valor_linhas_pares_matriz(m):
    for i in range(0,len(m),2):
        for j in range(len(m[i])):
            m[i][j] = 1
    return m

def altera_valor_colunas_impares(m):
    for j in range(1,len(m[0]),2):
        for i in range(len(m)):
            m[i][j] = 2
    return m

def altera_valor_colunas_pares(m):
    for j in range(0,len(m),2):
        for i in range(len(m)):
            m[i][j] = 1
    return m

def soma_matrizes(m1,m2):
     cria_matriz(3,3)
     for i in range(len(m1)):
         for j in range(len(m1[0])):
            m = m1[i][j] + m2[i][j]
            matriz[i][j] = m
         return matriz

def tabuleiro(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i%2==j%2:
                matriz[i][j] = 0
            else :
                matriz[i][j] = 1
    return matriz

def transpoe_matriz(m):
    for i in range(len(m)):
        for j in range(i):
            aux = m[i][j]
            m[i][j]= m[j][i]
            m[j][i] = aux

        return mostra_matriz(m)
def soma_lista(lista):
    soma = 0
    for elem in lista:
        soma+=elem
    return soma
def multiplica_matriz():
    alunos = 10
    notas = cria_matriz(5,alunos)
    pesos = [1,2,3,2,1]
    soma_pesos = soma_lista(pesos)
    medias = []
    mostra_matriz(notas)
    for j in range(alunos):
        soma = 0
        for i in range(len(pesos)):
            soma += pesos[i]*notas[i][j]
        media = soma/soma_pesos
        medias.append(media)
    print(medias)

matriz = cria_matriz(5,10)

peso = [1,2,3,2,1]
Soma = 0
for i in range(len(peso)):
  Soma += peso[i]*matriz[i][0]

mostra_matriz(matriz)
print(Soma)



