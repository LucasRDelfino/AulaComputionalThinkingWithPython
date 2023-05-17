def teste_numerico(frase):
    var = input(frase)
    while not var.isnumeric():
        var = input(frase)
    var = int(var)
    return var

def teste_par(num) :
    if num%2==0 :
        return True
    else :
        return False

def vogal (letra):
    qtd_vogais = 0
    if letra in ["a","e","i","o","u"] :
        qtd_vogais += 1
        print(f"{letra} é vogal")
    else :
        print(f"{letra} é uma consoante")
    return qtd_vogais

def soma (num1,num2):
    return num1+num2

def subtracao (num1,num2):
    return num1-num2

def multiplicacao (num1,num2):
    return num1*num2 

def divisao (num1,num2):
    return num1/num2

def numerico (frase):
    num = input(frase)
    while not num.isnumeric()  :
            print ("Você digitou algum valor errado digite apenas numeros")
            num = input (frase)
    return int(num)

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

def media(valores):
    total = 0
    for valor in valores:
        total += valor
    return total/len(valores)

def meu_input_numerico():
    num = input("Digite um numero :")
    if num.isnumeric():
        num = int(num)
        return num
    else :
        return meu_input_numerico()








