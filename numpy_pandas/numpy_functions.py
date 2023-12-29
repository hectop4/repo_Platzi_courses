import numpy as np

arr=np.random.randint(1, 10, size=(3, 3))
matriz=arr.reshape(1,9)
print(arr)
4

#Max
print(np.max(arr))#retorna el valor maximo del array
print(np.max(0))#retorna el valor maximo de cada columna

print(arr.max(1))#retorna el valor maximo del array

#Min

print(arr.min())#retorna el valor minimo del array
print(arr.min(0))#retorna el valor minimo de cada columna
print(arr.argmin())#retorna el indice del valor minimo del array

#ptp
print(arr.ptp())#retorna la diferencia entre el valor maximo y el minimo del array

#percentile
print(np.percentile(arr,50))#retorna el percentil del array Percentile es valor del medio

#sort
print(np.sort(arr))#retorna el array ordenado
print(np.sort(matriz))#retorna el array ordenado

#median
print(np.median(arr))#retorna la mediana del array
print(np.median(matriz))#retorna la mediana del array

#std

print(np.std(arr))#retorna la desviacion estandar del array
print(np.std(matriz))#retorna la desviacion estandar del array

#var

print(np.var(arr))#retorna la varianza del array
print(np.var(matriz))#retorna la varianza del array

#mean

print(np.mean(arr))#retorna la media del array
print(np.mean(matriz))#retorna la media del array

#sum

print(np.sum(arr))#retorna la suma del array
print(np.sum(matriz))#retorna la suma del array

#concatenate

arr1=np.random.randint(1, 10, size=(3, 3))
arr2=np.random.randint(1, 10, size=(3, 3))
print(arr1)
print(arr2)
print("_"*50)
print(np.concatenate((arr1,arr2),axis=0))#concatena los arrays

#transpose
print(arr1)
print(arr1.transpose())#transpone el array
