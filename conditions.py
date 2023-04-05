#EX1

n1 = int(input("Digite o primeiro numero"))
n2 = int(input("Digite o segundo numero"))
n3 = int (input ("Digite o terceiro numero"))
n4 = int (input ("Digite o quarto numero"))

if n1>n2 and n1>n3 and n1>n4: 
    print(f"O maior numero é {n1}")
elif n2>n3 and n2>n4 :
    print (f"O maior numero é {n2}")
elif n3>n4 :
    print (f"O maior numero é {n3}")
else :
    print (f"O maior numero é {n4}")


#EX2 

n1 = int(input("Digite o primeiro numero"))
n2 = int(input("Digite o segundo numero"))
n3 = int (input ("Digite o terceiro numero"))
n4 = int (input ("Digite o quarto numero"))


resposta = int(input("O que você deseja descobrir no programa? 1.Maior Número 2.Menor número"))

if resposta==1 :
    if n1>n2 and n1>n3 and n1>n4: 
        print(f"O maior numero é {n1}")
    elif n2>n3 and n2>n4 :
        print (f"O maior numero é {n2}")
    elif n3>n4 :
        print (f"O maior numero é {n3}")
    else :
        print (f"O maior numero é {n4}")

else : 
    if n1<n2 and n1<n3 and n1<n4: 
        print(f"O menor numero é {n1}")
    elif n2<n3 and n2<n4 :
        print (f"O menor numero é {n2}")
    elif n3<n4 :
        print (f"O menor numero é {n3}")
    else :
        print (f"O menor numero é {n4}")


#EX3

n = int(input("Digite o numero de amaciantes que você deseja comprar"))
cadastro = input("Você possui cadastro na loja?")


if n>100 and cadastro=="sim" :
    print(f"O total da sua compra é igual a {n*0.30}")
elif n>100 or cadastro=="sim" :
    print(f"O total da sua compra é igual a {n*0.35}")
else :
    print(f"O total da sua compra é igual a {n*0.50}")

#while
i = 1
soma = 0
while i < 11 :
    soma += i 
    i+=1
    print(soma)
