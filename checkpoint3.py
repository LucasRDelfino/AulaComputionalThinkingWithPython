def checa_opcoes(frase,opcoes_cadastradas):
    escolha = input (frase)
    while not escolha in opcoes_cadastradas:
        escolha = input ("Digite a operação que quer realizar : 1.soma 2.subtracao 3.multiplicacao 4.divisao")
    return escolha

def acha_maior(valores,nomes):
    indice_maior = 0
    maior = valores[0]
    for i in range(len(valores)):
        if valores[i] > maior:
            indice_maior = i
            maior = valores[i]
    return nomes[indice_maior]

def acha_menor(valores,nomes):
    indice_menor = 0
    menor = valores[0]
    for i in range(len(valores)):
        if valores[i] < menor:
            indice_menor = i
            menor = valores[i]
    return nomes[indice_menor]

vinhos = ["rose","tinto","branco","cheiroso","fedido"]

precos = [100,200,300,1000,50]


opcao = checa_opcoes("Quer descobrir o menor ou maior?",["maior","menor"])
if opcao == "maior" :
    print(acha_maior(precos,vinhos))
else :
    print(acha_menor(precos,vinhos))