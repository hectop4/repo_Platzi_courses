import numpy as np
#Problemas con la copia de arrays
arr = np.arange(1, 10)
print(arr)
print(arr.ndim)
parr=arr[:4]
print(parr)

parr[:]=0
print(parr)
print(arr)
arr = np.arange(1, 10)
arrcp=arr.copy()
print(arrcp)

arrcp[:]=0
print(arrcp)
print(arr) 