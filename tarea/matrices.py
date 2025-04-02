matriz1= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [5, 2, 6],
    [1, 3, 4],
    [7, 8, 9]
]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(columnas)] for i in range(filas)]
    return resultado

print("matriz 1: ")
mostrar_matriz(matriz1)

print("matriz 2: ")
mostrar_matriz(matriz2)

print("la suma de las matrices es: ")
suma = sumar_matrices(matriz1, matriz2)
mostrar_matriz(suma)
