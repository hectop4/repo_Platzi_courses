#Enumeracion exhaustiva busca todas las posibilidades hasta encontrar la respuesta
#Si no es una solucion exacta no la encuentra, pero podemos aproximarla

objetivo=int(input('Escoge un entero: '))
respuesta=0

while respuesta**2<objetivo:
    print(respuesta)
    respuesta+=1
if respuesta**2==objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')