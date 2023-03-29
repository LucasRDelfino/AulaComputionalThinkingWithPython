
# EX1
i = 1
soma = 0
while i<=10 :
    soma += i
    i+=1
    print(f"O valor da soma é igual a{soma}")



# EX2
i = 1
while i<=5:
    n = int(input("Digite um número"))
    if n%2== 0 :
        print (f"O numero {n} é par")
    else:
        print (f"O numero {n} é impar")
    i += 1



# EX3  
verificacao = input ("Você quer verificar se a letra é vogal ou consoante? 1.Sim 2.Não")
if verificacao =="1" or verificacao == "sim" or verificacao == "Sim":
    letra = input(f'Digite uma letra(escreva "sair" para parar o programa):') 
    while letra!="sair":
        if letra=="a" or letra=="e" or letra=="i" or letra=="u":
            print("A letra digitada é uma vogal")

        else:
            print("A letra digitada é uma consoante")
        letra = input(f'Digite uma letra(escreva "sair" para parar o programa):') 

else : 
    print("Bobão")

# EX4
verificacao = False;
i = 0;
while verificacao==False : 
    usuario = input ("Digite o usuario : ")
    senha = input ("Digite a senha")
    i+=1;
    if i<3 : 
        if usuario == "lucas" and senha == "lucas123" :
            print("Usuário e senha corretos")
            verificacao = True
        else :
            print("Usuario ou senha foram diigtados de forma incorreta, tente novamente")
    else : 
        print("Máximo de tentativas excedido")

# EX4.1
usuario = "lucas"
senha = "1234"

user = input ("Digite o seu usuario")
password = input ("Digite a senha")
i = 0
while (usuario!=user and password!=senha) and i<=2 :
      print ("Acesso negado")
      user = input ("Digite o seu usuario")
      password = input ("Digite a senha")
      i+=1
    
if i==2:     
   print("Acesso concedido")


