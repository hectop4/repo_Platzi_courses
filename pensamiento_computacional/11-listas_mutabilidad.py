#Son secuencias de objetos que son mutables
#Al ser mutables puede haber side effects que den espacio a errores
#Para modificar una lista se puede usar el metodo append o el metodo insert 
#o el metodo extend o el metodo pop o el metodo remove o el metodo clear o el mismo indice de la lista

a = [1,2,3]
b=a
c=[a,b]
a.append(5)

print(a)
print(b)        #Al ser mutables, al modificar a, tambien se modifica b
print(c)


#Para copiar una lista se puede usar el metodo copy o el metodo list

a = [1,2,3]
b=a
c=list(a)


d=a[::]
print(id(a),id(b),id(c),id(d))

#List comprehension
#Es una forma de crear listas de forma mas eficiente
#Tambien se puede aplicar condiciones para filtrar

my_list = list(range(100))
print(my_list)


double=[i*2 for i in my_list]

print(double)

pares=[i for i in my_list if i%2==0]
print(pares)