import numpy as np

# Crear arrays y operaciones básicas
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
suma = a + b          # [5, 7, 9]
producto = a * 2      # [2, 4, 6] (broadcasting)

# Matrices y operaciones avanzadas
matriz = np.array([[1, 2], [3, 4]])
determinante = np.linalg.det(matriz)  # -2.0 (1*4 - 2*3)

# Indexación y filtrado
print(matriz[1, 0])   # 3 (fila 1, columna 0)
print(a[a > 2])       # [3] (elementos > 2)

print("Suma:", suma)
print("Determinante:", determinante)