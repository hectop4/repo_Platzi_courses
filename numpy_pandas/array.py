import numpy as np


#Array de una dimension
list = [1, 2, 3, 4, 5]
arr=np.array(list)
print(type(arr))

#Matriz de dos dimensiones

matriz=[[1,2,3],[4,5,6],[7,8,9]]
m=np.array(matriz)
print(m)
print(type(m))

#indexado
print(arr[0])
print(m[0,2])

#Slicing
print(arr[0:2]) #No incluye el ultimo elemento
print(m[0:2,0:2])
print(arr[0::2])# salta de dos en dos
print(arr[-1]) #ultimo elemento
print(m[-1,-1]) #ultimo elemento
print(m[-1,0:2]) #ultimo elemento
