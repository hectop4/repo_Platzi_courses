# Es un ordenamiento que divide la lista en sublistas hasta que cada sublista
# tenga un solo elemento y luego las va comparando entre ellas hasta que se
# ordenen de menor a mayor
import random

def ordenamiento_mezcla(lista):
    if len(lista)>1:
        medio=len(lista)//2
        izquierda=lista[:medio]
        derecha=lista[medio:]

        #Llamada recursiva en cada mitad
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)
        #Iteradores para recorre las dos sublistas
        i=0
        j=0
        #Iterador para la lista principal
        k=0
        while i<len(izquierda) and j<len(derecha):
            if izquierda[i]<derecha[j]:
                lista[k]=izquierda[i]
                i+=1
            else:
                lista[k]=derecha[j]
                j+=1
            k+=1
        while i<len(izquierda):
            lista[k]=izquierda[i]
            i+=1
            k+=1
        while j<len(derecha):
            lista[k]=derecha[j]
            j+=1
            k+=1
    return lista


if __name__=='__main__':
    tamano_de_lista=int(input('De que tamano sera la lista? '))
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    print('-'*20)
    lista_ordenada=ordenamiento_mezcla(lista)
    print(lista_ordenada)