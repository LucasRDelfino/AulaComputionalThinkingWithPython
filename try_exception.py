 # lista = [4,5,6,7,9]
# while True:
#     try:
#         i  = int(input("Diga um número : "))
#         print(lista[i])
#     except ValueError:
#         print("Voce não digitou um inteiro!")
#     except IndexError:
#         print(f"Deve ser entre 0 e {len(lista)-1}")
#     except Exception as e:
#         print(e)
#     else:
#         print("Operação realizada com sucesso")
#         break
#     finally:
#         print("N sirvo pra mta coisa")

#Reescreva utilizando tratamento de exceções:
# while True:
#     try:
#         flag = "primeiro"
#         a = int(input("Diga o primeiro numero : "))
#         flag = "segundo"
#         b = int(input("Diga o segundo numero : "))
#         resultado = b/a
#     except ValueError:
#         print(f"O {flag} número está errado!")
#     except ZeroDivisionError:
#         print("O primeiro número não pode ser zero!")
#     else:
#         print(resultado)
#         break

#Reescreva utilizando tratamento de exceções:
# times = {
#     'são paulo' : 'campeão',
#     'corinthians' : 'sem tite',
#     'palmeiras' : 'sem mundial',
#     'santos' : 'idoso rebaixado'
# }
# while True:
#     time = input("Diga seu time : ")
#     try:
#         print(f"Você é um {times[time]}")
#         break
#     except KeyError:
#         print(f"Selcione uma opção entre {times.keys()} ")
#     else:
#         print(f"Vc deve digitar um desses : {times.keys()}")

def acha_maior(lista):
    maior = lista[0]
    indice_maior = 0
    if type(lista) is not list:
        raise TypeError("O parâmetro da função tem que ser uma lista")
    for i in range(len(lista)):
        if type(i) not in [int,float]:
            raise TypeError("A lista tem que conter apenas números")
        if lista[i] > maior:
            indice_maior = i
            maior = lista[i]
    return indice_maior

lista = [10,2,3,5,4]

def ordena(lista):
    ordenada = []
    while lista:
        print(lista)
        print(ordenada)
        indice = acha_maior(lista)
        maior = lista.pop(indice)
        ordenada.append(maior)
    return ordenada


for i in range(len(lista)):
    indice_delay = acha_maior(lista[i:])
    print(lista[i:],indice_delay)
    indice_real = indice_delay+i
    aux = lista[i]
    lista[i] = lista[indice_real]
    lista[indice_real] = aux
    print(lista)




