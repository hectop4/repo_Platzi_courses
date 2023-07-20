#Las afirmaciones son una forma de asegurarnos que un código se cumpla
#Es un metodo de programacion defensiva
#Normalmente se usa para verificar que los tipos de datos sean correctos
#Se usa para debuggear
#Se usa assert
#Se puede usar para verificar que una lista no este vacia
#Se puede usar para verificar que un valor no sea None

def primera_letra(lista_de_palabras):
    primera_letra = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'
        primera_letra.append(palabra[0])

    return primera_letra

lista = ['Angel', 2, 'ljhkhu', 'Carlos']
print('Primeras letras validas son: ', primera_letra(lista))