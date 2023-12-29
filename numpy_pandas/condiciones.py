import numpy as np

arr=np.linspace(1, 10, 10,dtype='int8')

print(arr)

#condiciones
indices_cond=arr>5#retorna un array de booleanos en base a la condicion

print(indices_cond)

print(arr[indices_cond])#retorna los valores que cumplen la condicion

print(arr[(arr>5) & (arr<9)])#retorna los valores que cumplen la condicion

arr[arr<5]=99 #asigna un valor a los valores que cumplen la condicion


print(arr)
