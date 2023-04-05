#EX1

escolha = int(input("Digite a ação desejada 1.Cadastrar 2.Ver estoque 3.Promoções 4.Sair"))

if escolha==1 :
    print("Cadastro realizado com sucesso")
elif escolha==2 :
    print("Dez caixas no estoque")
elif escolha==3 :
    print("Compre uma caixa leva duas")
else : 
    print("Clique duas vezes para sair da página")

#EX2

letra = input("Digite uma letra")

if letra=="a" or letra=="e" or letra=="i" or letra=="u":
    print("A letra digitada é uma vogal")

else:
    print("A letra digitada é uma consoante")


#EX3

n1 =  float(input("Digite a primeira nota"))

n2 = float (input("Digite a segunda nota"))


if n1<=10 and n2<=10 :
    media = (n1+n2)/2
    if media>4 : 
        print(f"Reprovado, média: {media}")
    elif media<6 :
        print (f"Recuperação, média: {media}")
    else :
        print(f"Aprovado, média: {media}")
else : 
    print("Digite notas entre 0 e 10")


#EX4

resposta = int(input("Você quer conhecer minha calculadora?1.Sim 2.Nao"))
if resposta==1:
    n1 = float(input("Digite o primeiro numero"))
    n2 = float (input("Digite o segundo numero"))
    operacao = int(input("Qual operacao quer realizar? 1.Adicao 2.Subtracao 3.Multiplicacao 4.Divisao"))
    if operacao==1 :
        resultado = n1+n2
        print(f"O resultado da soma é igual a {resultado}")
    elif operacao==2 : 
        resultado = n1-n2
        print(f"O resultado da subtracao é igual a {resultado}")
    elif operacao==3 :
        resultado = n1*n2
        print(f"O resultado da multiplicacao é igual a {resultado}")
    else :
        resultado = n1/n2
        print(f"O resultado da divisao é igual a {resultado}")
else :
    print("Eu nem queria mesmo.....")


#EX5

n1 = int(input("Digite o primeiro numero"))
n2 = int(input("Digite o segundo numero"))
n3 = int (input ("Digite o terceiro numero"))

if n1>n2 and n1>n3 : 
    print(f"O maior numero é {n1}")
elif n2>n3 and n2>n1 :
    print (f"O maior numero é {n2}")
else :
    print (f"O maior numero é {n3}")





    
