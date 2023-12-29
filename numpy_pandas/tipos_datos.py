import numpy as np

# Tipos de datos en Python
arr=np.array([1, 2, 3, 4, 5])
print(arr.dtype) #int64

arr=np.array([1, 2, 3, 4, 5],dtype='float64')
print(arr) #float64
print(arr.dtype) #float64

arr=np.array([1, 2, 3, 4, 5])
print(arr.dtype) #int64
arr=arr.astype(np.float64)
print(arr.dtype) #int64

arr=np.array([1, 2, 3, 4, 5])
arr=arr.astype(np.bool_)
arr=arr.astype(np.int64)
arr=arr.astype(np.float64)
arr = arr.astype(np.str_)
print(arr) #bool
print(arr.dtype) #int64