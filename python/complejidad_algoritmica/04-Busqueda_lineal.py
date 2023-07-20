#Busca en todos los elementos de manera secuencial
#El peor de los casos es que el elemento no exista en la lista
#O(n)
import random  

def busqueda_lineal(lista, objetivo):
    match=False

    for elemento in lista:
        if elemento ==objetivo:
            match=True
            break
    return match

if __name__=='__main__':
    tamano_de_lista=int(input('De que tamano sera la lista? '))
    objetivo=int(input('Que numero quieres encontrar? '))

    lista=[random.randint(0,100) for i in range(tamano_de_lista)]

    encontrado=busqueda_lineal(lista,objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

    #La complejidad de este algoritmo es lineal, O(n)