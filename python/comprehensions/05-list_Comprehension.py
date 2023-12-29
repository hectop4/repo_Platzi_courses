# Es una forma de crear listas de forma rápida, sencilla y legible.
numbers = []

#Quiero una lista con cada uno de los números elevados al cuadrado
for element in range(1,11):
    numbers.append(element)
print(numbers)

#List comprehension permite simplificar lo anterior en una sola línea

numbers_2=[element for element in range(1,11)]
print(numbers_2)

#Quiero una lista con cada uno de los números elevados al cuadrado

numbers_3=[element**2 for element in range(1,11)]
print(numbers_3)

#[elemento for elemento in iterable condición]
#[elemento for elemento in iterable condición if condición]
#La condicion permite filtrar los elementos que se van a agregar a la lista

for i in range(1,11):
    if i%2==0:
        print(i)

#Lo anterior se puede simplificar en una sola línea:
numbers_4=[element for element in range(1,11) if element%2==0]
print(numbers_4)
