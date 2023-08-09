# EX 1
# senha = "12345"
# senha_usuario = input("Digite sua senha :")
# i = 1
# while senha != senha_usuario and i<3:
#     print ("errouuuuu")
#     senha_usuario = input("Digite sua senha :")
#     i += 1
#
# if senha == senha_usuario:
#     print("Acesso liberado")
# else :
#     print("sai")

# EX 2
# def acha_maior(lista) :
#     indice_maior = 0
#     maior = lista[indice_maior]
#     for i in range(len(lista)):
#         if lista[i]>maior:
#             indice_maior = i
#         return lista[indice_maior]
#
# precos = [1000,2000,3000,4000]
# print(acha_maior(precos))

# EX 3
# lista1 = ["Lucas","Pedro","Luisa"]
# lista2 = ["Gabriel","Lucas","Gustavo"]
# lista3 = []
# for nome in lista1:
#     if nome in lista2 :
#         lista3.append(nome)
#
# print(lista3)

# EX 4
def inverte_lista(lista):
    ultimo = len(lista)-1
    for i in range(len(lista))//2:
        aux = lista[i]
        lista[i] = lista[ultimo-i]
        lista[ultimo-1]= aux
        return lista
