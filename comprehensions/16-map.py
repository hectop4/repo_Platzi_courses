#Map es una funcion que recibe una funcion y un iterable, y 
#devuelve un iterable con la funcion aplicada a cada elemento del iterable
numbers = [1, 2, 3, 4, 5]

#Map en 3 lineas
numbers_v2=[]
for i in numbers:
    numbers_v2.append(i**2)

print(numbers)
print(numbers_v2)
#Map en 1 linea
numbers_v3=map(lambda i: i**2,numbers)

print(list(numbers_v3))

numbers_1=[5, 6, 7, 8, 9]
numbers_2=[1, 2, 3, 4, ]
#Este obtiene el menor de los dos iterables
reslut = list(map(lambda x,y: x+y, numbers_1, numbers_2))
print(reslut)
