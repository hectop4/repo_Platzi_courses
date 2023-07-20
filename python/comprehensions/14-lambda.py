def increment(x):
    return x + 1

print(increment(2))
#Lambda es una funcion anonima
#eso quiere decir que no tiene nombre
#pero se puede asignar a una variable

result = increment(2)
print(result)

#Debemos conoconer los paramentros de entrada y salida

increment_v2=lambda x: x + 1 #x es el parametro de entrada y x + 1 es el retorno

result2 = increment_v2(4)
print(result2)

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
text=full_name('guido', 'van rossum')
print(text)
print(full_name('guido', 'van rossum'))