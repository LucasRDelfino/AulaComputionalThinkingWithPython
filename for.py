# #EX1
# for i in range(100) :
#     if i%2==0:
#         print(f"Número {i} é par")
#     else :
#         print(f"Número {i} é impar")

# #EX2
# for num in range(1,11) : 
#     for i in range(1,11) :
#         print(f"{num}*{i}={i*num}")

# #EX3
# soma = 0
# for num in range(1,11):
#     soma += int(input("Digite o número desejado"))


# print (f"O valor da soma é {soma} e a média {soma/10}")

# #EX4
# usuario = "lusquinhas"
# senha = "lusquinhas123"

# for i in range(3) :
#     user_name = input("Digite o usuario")
#     user_password = input("Digite a senha")
#     if usuario==user_name and senha==user_password :
#         print("Você entrou no sistema")
#         break
#     print("Senha inválida , tente novamente")

# print("Você atingiu o número de tentativas")

#EX5

tamanho = int(input("Digite o tamanho da lista :"))
list = []

for i in range(tamanho):
    num = int(input("Digite um numero para ser adicionado a lista"))
    list.append(num)
print(list)