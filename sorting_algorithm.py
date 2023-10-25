def acha_menor(lista):
    indice_menor = 0
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            indice_menor = i
            menor = lista[i]
    return indice_menor


def selection_sort(lista):
    ordenada = []
    while lista:
        print(lista)
        print(ordenada)
        indice = acha_menor(lista)
        maior = lista.pop(indice)
        ordenada.append(maior)
    return ordenada

def selection_sort_ruim(lista):
    for i in range(len(lista)):
        indice_delay = acha_menor(lista[i:])
        print(lista[i:],indice_delay)
        indice_real = indice_delay+i
        aux = lista[i]
        lista[i] = lista[indice_real]
        lista[indice_real] = aux
    return lista


def selection_sort_medio(lista) :
    for j in range(len(lista)):
        n_trocas = 0
        for i in range(len(lista)-j-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                n_trocas += 1
            print(lista)
        if n_trocas == 0:
            break
    return lista

def binary_search_sqrt(num):
    inicio = 0
    fim = num
    chute = (inicio+fim)/2
    qtd = 0
    while abs(chute**2 - num) >= 0.001:
        if chute**2 > num:
            fim = chute
        else:
            inicio = chute
        qtd+=1
        chute = (inicio+fim)/2
    print(chute,chute**2,num,qtd)
    return

binary_search_sqrt(25)


