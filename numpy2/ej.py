# Matrices y operaciones avanzadas
matriz = np.array([[1, 2], [3, 4]])
determinante = np.linalg.det(matriz)  # -2.0 (1*4 - 2*3)

# Indexación y filtrado
print(matriz[1, 0])   # 3 (fila 1, columna 0)
print(a[a > 2])       # [3] (elementos > 2)

print("Suma:", suma)
print("Determinante:", determinante)

import numpy as np 
import random 
num=random.randint(5,10)
lista=[random.randint(1,100) for i in range(num)]
print(lista)
arreglo=np.array(lista)
print(arreglo)
print(type(arreglo))
#array bidimensional
matrix=np.array([[10,20,30],[50,70,60]])
print(matrix)
ceros=np.zeros ((3,3))
print(ceros)
unos=np.ones((3,2))
print(unos) 
vec1=np.arange(10,-1,-1)
print(vec1)
matrixt=np.array([[1,2],[3,4],[5,6]])
print(matrixt)
print("dimensiones vector",vec1.ndim)
print("dimensiones",matrixt.ndim)
print("forma",matrixt.shape)
print("tam",matrixt.size)
matrixt.dtype
lista1=[random.randint(1,100) for i in range(5)]
lista2=[random.randint(1,100) for i in range(5)]
print(lista1)
print(lista2)
a=np.array(lista1)
b=np.array(lista2)
print("suma=",a+b)
print("multiplicacion=",a*b)
esc=a*10
print(esc)