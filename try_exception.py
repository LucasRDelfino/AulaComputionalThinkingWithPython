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

