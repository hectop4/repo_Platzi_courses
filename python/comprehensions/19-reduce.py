#Reduce se encarga de reducir una lista a un solo valor
#Reduce no es una función nativa de python, por lo que debemos importarla
import functools
from functools import reduce


numbers=[1,2,3,4,5,6,7,8,9,10]

result = functools.reduce(lambda acumulator, element: acumulator+element,numbers)

def accum(counter,item):
    print(counter)
    print(item)
    return counter+item


print(result)
print("*************"*15)


#Reduce recibe una función y una lista
#La función que recibe reduce debe recibir dos parámetros
#El primer parámetro es el acumulador
#El segundo parámetro es el elemento de la lista

