#EX1
v1 = float(input("Digite o valor do amaciante"))

desc = float(input("Digite o valor do desconto"))

desc = ((100-desc)/100)*v1

val_desc = v1-desc

print (f"O valor a se pagar com desconto é igual a {desc}")

print (f"O valor de desconto é igual a {val_desc} ") 

#EX2

a = 2
b = 3

xa = (b-a)+a 
xb = (a-b)+b

#ou
a2 = "joão"
b2 = "lucas"

q = a2;
a2=b2;
b2 = q;

print(xa,xb)
print(a2,b2) 

#EX4

salario = float(input("Digite seu salário"))

if salario<1903.98 :
    print("Você está insento de pagar o imposto de renda")
elif salario>1903.99 and salario<2826.65:
    print("Sua taxa no imposto de renda  é de 7,5%")
elif salario>2826.66 and salario<3751.05:
    print("Sua taxa no imposto de renda  é de 15%")
elif salario>3751.06 and salario<4664.68:
    print("Sua taxa no imposto de renda  é de 22,5%")
else : 
    print("Sua taxa no imposto de renda é de 27,5%")
