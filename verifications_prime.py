#EX1.1
# n = int (input ("Digite o número que quer verificar:"))
# i = 2
# while i <= n : 
#       if (n%i == 0) :          
#         print("O número não é primo")
#         break
#       elif i >= n/2: 
#         print(f"O número é primo")
#         break
#       i+=1


#EX1.2
# n = int (input ("Digite o número que quer verificar:"))
# i = 2
# while i <= n : 
#       if (n%i == 0) :          
#         print("O número não é primo")
#         break
#       elif i>=num**(1/2): 
#         print(f"O número é primo")
#         break
#       i+=1
        
        

# EX2
# n = 0

# while n<100 :
#     n += 1
#     i = 2
#     while i < n : 
#         if (n%i == 0) :
#            break
#         elif i >= n/2: 
#             print(n)
#             break
#         i += 1
        
#EX3
qtd = 2
a = 1
b = 1
while qtd<100 :
    c = a+b
    a = b
    b = c
    i = 2
    while i < c : 
        if c%i == 0 :
          print(f"O número {c} não é primo")
          break
        elif i>=c**(1/2):
          print(f"O número {c} é primo")
          break
        i += 1
    qtd +=1
        





