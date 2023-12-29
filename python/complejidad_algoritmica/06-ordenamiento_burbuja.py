#Es un algoritmo que recorre todos los elementos de una lista 
#y los va comparando con el objetivo hasta que se ordene de menor a mayor
#y se encuentre el objetivo o se llegue al final de la lista


import random

def ordenamiento_burbuja(lista):#O(n^2)=cuadratica
    n=len(lista)
    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista

if __name__=='__main__':
    tamano_de_lista=int(input('De que tamano sera la lista? '))
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    
    lista_ordenada=ordenamiento_burbuja(lista)
    print(lista_ordenada)