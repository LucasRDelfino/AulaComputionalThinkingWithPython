# list = [i for i in range(1,11)] 

# for i in range(len(list)):
#     print(list[i])


professores = ["Eduardo","Israel","Danilo","Cordeiro","Ana"]

for i in range(len(professores)):
    if professores[i]=="Danilo":
        print(f"{professores[i]} é o melhor professor")
        break
    print(professores[i])