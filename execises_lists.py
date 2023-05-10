# #EX1
numeros = [234,546,567,523467,2343,54234]
contagem = 0
for i in range(len(numeros)) :
    if numeros[i]%2==0 :
        contagem+=1


print(f"Tem {contagem} numeros pares na lista")

#EX2
num1 = [1,2,3,4,5]
num2 = [1,2,3,4,5]
num3 = []

for i in range(len(num1)):
    soma = num1[i] + num2[i]
    num3.append(soma)

print(num1)
print(num2)
print(num3)

#EX3.1
letras = ["a","b","c","d","i","o","h"]
contagem = 0 
for i in range(len(letras)):
    if letras[i]=="a" or  letras[i]=="e" or  letras[i]=="i" or  letras[i]=="o" or letras[i]=="u":
        contagem+=1
print(f"Tem {contagem} vogais na lista")

#EX3.2
letras = ["a","b","c","d","i","o","h"]
vogais = 0
for letra in letras:
    if letra in ["a","e","i","o","u"]:
        vogais += 1

#EX4
profs = ["allen","israel","danilo","Yan","luciano","ana","cordeiro"]

for i in range(len(profs)):
    if profs[i]=="danilo":
        print(f"Danilo está na posição {i+1} da lista")
        break


#EX5
carros = ["ka","celta","golf","fusca"]
preco = [10,1000,200,5]

maior = preco[0]
for i in range(len(preco)):
    if preco[i]>maior:
        maior = preco[i]
        indice_maior = i
print(f"O carro mais caro é o {carros[indice_maior]}")

#EX6
letras = ["a","b","c","d","i","o","h"]
ultimo = len(letras)-1
for i in range(len(letras)):
    temporaria = letras[i]
    letras[i] = letras[ultimo]
    letras[ultimo] = temporaria
    ultimo -= 1

print(letras)