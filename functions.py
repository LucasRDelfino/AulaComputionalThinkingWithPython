def teste_numerico(frase):
    var = input(frase)
    while not var.isnumeric():
        var = input(frase)
    var = int(var)
    return var

def teste_par(num) :
    if num%2==0 :
        return True
    else :
        return False

for i in range(10) :
    numero = teste_numerico("Diga um numero :")
    if teste_par(numero):
        print(f"O {numero} é par")
    else :
        print(f"O {numero} é impar")