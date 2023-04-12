#EX1
# resposta = input("Digite um número")

# while not resposta.isnumeric() : 
#     print("Você não digitou um número , tente novamente")
#     resposta = input("Digite um número")


# resposta = int(resposta)
# print ("ACERTOUUUUU")


resposta = input ("Você quer usar a calculadora s/n")

while resposta!="s" and resposta!="n" :
    resposta = input ("Você digitou errado , digite s/n")

if resposta=="s" : 
    
    while True :
        n1 = input ("Digite um número")
        n2 = input ("Digite outro número")

        while not n1.isnumeric() or not n2.isnumeric() :
            print ("Você digitou algum valor errado digite apenas numeros")
            n1 = input ("Digite um número")
            n2 = input ("Digite outro número")

        operacao = input ("Digite a operacao desejada na calculadora 1.Adição 2.Subtração 3.Multiplicação 4.Divisão 5.Sair")

        while not (operacao=="1" or operacao=="2" or operacao=="3" or operacao=="4" or operacao=="5") :
            operacao = input ("Você digitou alguma coisa errada , escolha entre 1.Adição 2.Subtração 3.Multiplicação 4.Divisão 5.Sair")

        n1 = float(n1)
        n2 = float(n2)
        operacao = int(operacao)

        if operacao==1 :
                resultado = n1+n2
                print(f"O resultado da soma é igual a {resultado}")
        elif operacao==2 : 
                resultado = n1-n2
                print(f"O resultado da subtracao é igual a {resultado}")
        elif operacao==3 :
                resultado = n1*n2
                print(f"O resultado da multiplicacao é igual a {resultado}")
        elif operacao==4:
                resultado = n1/n2
                print(f"O resultado da divisao é igual a {resultado}")
        else :
            print("Você saiu do programa")
            break

else : 
    print ("BLZ VACILÃO")

