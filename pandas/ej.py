#CopiarEditar
import pandas as pd

# Serie
serie = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# DataFrame
df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis'],
    'Edad': [25, 30]
})

# Ver primeras filas
print(df.head())

# Seleccionar columna
print(df['Nombre'])

# Seleccionar fila por índice
print(df.loc[0])

# Añadir columna
df['Ciudad'] = ['Lima', 'Bogotá']

# Modificar un valor
df.at[0, 'Edad'] = 26

# Eliminar filas con valores nulos
df.dropna()

# Rellenar valores nulos
df.fillna('Desconocido')

# Edad promedio
print(df['Edad'].mean())

# Aplicar función
df['Edad2'] = df['Edad'].apply(lambda x: x * 2)

# Crear un nuevo DataFrame
df2 = pd.DataFrame({
    'Ciudad': ['Lima', 'Lima', 'Bogotá'],
    'Ventas': [100, 150, 200]
})

# Agrupar por ciudad y sumar ventas
print(df2.groupby('Ciudad')['Ventas'].sum())

# Combinar dos DataFrames por filas
df_comb = pd.concat([df, df], ignore_index=True)

# Unir por clave (merge)
df3 = pd.DataFrame({
    'Nombre': ['Ana', 'Luis'],
    'Salario': [1000, 1200]
})
print(pd.merge(df, df3, on='Nombre'))

df['Fecha'] = pd.to_datetime(['2023-01-01', '2023-05-15'])

# Extraer el año
df['Año'] = df['Fecha'].dt.year

import matplotlib.pyplot as plt

df['Edad'].plot(kind='bar')
plt.show()

# Tabla dinámica
pivot = df2.pivot_table(values='Ventas', index='Ciudad', aggfunc='sum')
print(pivot)
