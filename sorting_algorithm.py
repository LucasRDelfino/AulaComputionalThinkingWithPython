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


def bubble_sort(lista) :
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

def binary_search_sqrt(num, precisao):
    inicio = 0
    fim = num
    chute = (inicio+fim)/2
    qtd = 0
    while abs(chute**2 - num) >= precisao:
        if chute**2 > num:
            fim = chute
        else:
            inicio = chute
        qtd+=1
        chute = (inicio+fim)/2
    return chute, qtd

def binary_search_sqrt_recursiva(num, precisao , inicio , fim):
    chute = (inicio+fim)/2
    if abs(chute**2 - num) >= precisao:
        if chute**2 > num:
            fim = chute
        else:
            inicio = chute
        return binary_search_sqrt_recursiva(num, precisao, inicio, fim)
    return chute

def busca_binaria(lista, num, inicio, fim):
    chute = (inicio+fim)//2
    if lista[chute]==num:
        return chute
    if lista[chute]>num:
        fim = chute
        return busca_binaria(lista,num,inicio,fim)
    else:
        inicio = chute
        return busca_binaria(lista,num,inicio,fim)

def quick_sort(lista):
    if len(lista)<=1:
        return lista
    else:
        pivo = lista[0]
        menores = [elem for elem in lista if elem < pivo]
        maiores = [elem for elem in lista if elem > pivo]
        menores_ordenados = quick_sort(menores)
        maiores_ordenados = quick_sort(maiores)
        return menores_ordenados + [pivo] + maiores_ordenados

lista = [1,2,3,5,6,7,8,9]

print(busca_binaria(lista,9,0,8))




