#El margen de error lo llamamos epsilon
#El paso de aproximacion lo llamamos paso

#Ejemplo: Encontrar la raiz cuadrada de un numero aproximadamente

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