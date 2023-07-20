# Son listas pero con indices personalizados para cada elemento
# Se pueden modificar, agregar y eliminar elementos
# Se pueden agregar listas dentro de diccionarios
# Se pueden agregar diccionarios dentro de diccionarios
# Son mutables e iterables

my_dict = {
    'David': 35,
    'Erika': 32,
    'Jaime': 50
}
print(my_dict['David'])

my_dict.get('David',30) # Otra forma de obtener un valor, si no existe el valor, se puede agregar un valor por defecto

del my_dict['Jaime'] # Eliminar un elemento del diccionario
print(my_dict)

for llave in my_dict.keys(): # Imprimir las llaves del diccionario
    print(llave)

for value in my_dict.values(): # Imprimir los valores del diccionario
    print(value)

for llave, valor in my_dict.items(): # Imprimir las llaves y valores del diccionario
    print(llave, valor)

print('David' in my_dict) # Verificar si existe una llave en el diccionario

my_dict.clear() # Eliminar todos los elementos del diccionario
print(my_dict)