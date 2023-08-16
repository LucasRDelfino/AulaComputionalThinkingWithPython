import matplotlib.pyplot as plt

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
            matriz[i].append(0)
    return matriz
def altera_valor_linhas_pares_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i%2==0:
                m[i][j] = 1
    return m

def altera_valor_colunas_impares(m):
    for j in range(1,len(m[0]),2):
        for i in range(len(m)):
            m[i][j] = 2
    return m

def soma_matrizes(m1,m2):
     cria_matriz(3,3)
     for i in range(len(m1)):
         for j in range(len(m1[0])):
            m = m1[i][j] + m2[i][j]
            matriz[i][j] = m

         return matriz


def tabuleiro():
    matriz = cria_matriz(8,8)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i%2==0 and j%2==0:
                matriz[i][j] = 0
            else :
                matriz[i][j] = 1
    mostra_matriz(matriz)

def transpoe_matriz(m):
    for i in range(len(m)):
        for j in range(i):
            aux = m[i][j]
            m[i][j]= m[j][i]
            m[j][i] = aux

        return mostra_matriz(m)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
mostra_matriz(matriz)
print()
transpoe_matriz(matriz)



