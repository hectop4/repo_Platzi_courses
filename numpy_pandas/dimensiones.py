import numpy as np

scalar = np.array(5)
print(scalar)
print(scalar.ndim)

vector = np.array([1, 2, 3, 4, 5])
print(vector)
print(vector.ndim)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print(matrix.ndim)

tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [1, 2, 3]]])
print(tensor)
print(tensor.ndim)

tensor1=np.array([1,2,3] ,ndmin=10)
print(tensor1)
print(tensor1.ndim)

# Agregar o eliminar dimensiones

vector = np.array([1, 2, 3, 4, 5],ndmin=10)
print(vector)
print(vector.ndim)
expand=np.expand_dims(vector,axis=0)#axis=0 es la fila
expand1=np.expand_dims(vector,axis=1)#axis=1 es la columna Agregar dimensiones
print(expand)
print(expand.ndim)
print(expand1)
print(expand1.ndim)

print(vector, vector.ndim)
vector1=np.squeeze(vector,axis=0) #Eliminar dimensiones
vector2=np.squeeze(vector)#Elimina todas las dimensiones adicionales
print(vector1, vector1.ndim)
print(vector2, vector2.ndim)