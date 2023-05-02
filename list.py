#EX1
# list = [i for i in range(1,11)] 

# for i in range(len(list)):
#     print(list[i])

#EX2
# professores = ["Eduardo","Israel","Danilo","Cordeiro","Ana"]

# for i in range(len(professores)):
#     if professores[i]=="Danilo":
#         print(f"{professores[i]} é o melhor professor")
#         break
#     print(professores[i])


#EX3
# frase = ""
# list = ["dan","isra","cordeiro"]
# indice = 0
# for nomes in list :
#     if indice < len(list)-2:
#             frase += f"O {nomes}, "
#     elif indice == len(list)-2:
#             frase += f"{nomes} e "
#     else :
#         frase += f"{nomes} são professores"
#     indice+=1

# print(frase)

#EX4
nomes = ["dan","isra","cordeiro"]
teste = input ("digite um nome :")

for i in range(len(nomes)):
    if nomes[i]== teste:
        print(f"O nome está no indice {i} da lista")
        break
    else:
        print("Esse nome não está na lista")