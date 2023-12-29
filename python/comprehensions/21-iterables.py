for i in range(1, 11):
    print(i, end=" ")

my_iterable=iter(range(1, 4))
print(my_iterable)

print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
#print(next(my_iterable)) #Genera error porque no hay más elementos
#Generamos progresivamente los valores de la lista, de modo que ahorramos memoria
#y podemos trabajar con listas muy grandes
