def acha_maior(valores,nomes) :
    maior = lista[0]
    for i in len(valores):
        if valores[i]>maior:
            indice = i
            maior = valores[i]
    return nomes[indice_maior]
