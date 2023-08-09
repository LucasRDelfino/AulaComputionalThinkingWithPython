matriz = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j])


matriz2 = [ [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(len(matriz2)):
    for j in range(len(matriz2[0])):
        if i<j:
            matriz2[i][j] = 1
print(matriz2)



