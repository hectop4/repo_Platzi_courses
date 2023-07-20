#Abstraccion no es necesario saber como funciona internamente la funcion, sino que hace.
#Se usa para dividir el codigo en partes mas pequeñas y que sea mas facil de entender

#Decomposicion: Dividir el codigo en partes mas pequeñas

#Funcion para sumar
# def suma(a,b):
#     print('Se suman dos numeros')
#     resultado=a+b
#     return resultado

# print(suma(1,4))


##Funcion para usar los otros archivos

def busquedaBinario():
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
def aprox():
    objetivo=int(input('Escoge un entero: '))
    epsilon=0.01 #Margen de error

    paso=epsilon**2 #Paso de aproximacion
    respuesta=0.0

    while abs(respuesta**2-objetivo)>=epsilon and respuesta<=objetivo:
        
        respuesta+=paso

    if abs(respuesta**2-objetivo)>=epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
def enumeriacion():
    
    objetivo=int(input('Escoge un entero: '))
    respuesta=0

    while respuesta**2<objetivo:
        print(respuesta)
        respuesta+=1
    if respuesta**2==objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

func=input('Que funcion quieres usar? (busquedaBinario, aprox, enumeriacion): ')
if func=='busquedaBinario':
    busquedaBinario()
elif func=='aprox':
    aprox()
elif func=='enumeriacion':
    enumeriacion()
else:
    print('No se encontro la funcicon')