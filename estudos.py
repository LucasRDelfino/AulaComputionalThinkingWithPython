# def acha_maior(valores,nomes) :
#     maior = lista[0]
#     for i in len(valores):
#         if valores[i]>maior:
#             indice = i
#             maior = valores[i]
#     return nomes[indice_maior]

# frase = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
#
# frase = frase.replace(".","")
# frase = frase.lower()
# frase = frase.split(" ")
#
# print(frase)
# dic = {}
#
# for palavra in frase:
#     if palavra not in dic.keys():
#         dic[palavra] = 1
#     else:
#         dic[palavra] += 1
#
# print(dic)
#

lista= [1,2,3,4,5]

maior = lista[0]

for i in range(len(lista)):
    if i > maior:
        indice_maior = i
        maior = lista[i]

print(f"O maior número é {maior} e está no indice {i}")
