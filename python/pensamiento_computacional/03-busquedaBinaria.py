#Se usa cuando la lista esta ordenada
#Se divide la lista en dos y se busca en la mitad
#Solo funciona con listas ordenadas

objetivo=int(input('Escoge un numero: '))
epsilon=0.0000000000001
bajo=0.0
alto=max(1.0,objetivo)

respuesta=(alto+bajo)/2

while abs(respuesta**2-objetivo)>=epsilon:
    print(f'{bajo} es muy bajo, {alto} es muy alto, {respuesta} es la respuesta')
    if respuesta**2<objetivo:
        bajo=respuesta
    else:
        alto=respuesta
    respuesta=(alto+bajo)/2
print(f'La raiz cuadrada de {objetivo} es {respuesta}')
