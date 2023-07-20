#Las excepciones son errores que ocurren durante la ejecución del programa,
# pero no siempre son fatales
#Cuando no se manejan adecuadamente, pueden causar que el programa termine
# Se usa try , except y finally
#No deben manejarse de manera silecioas
#Se puede ramificar los programas
#raise aventar una excepcion propia

def divide_elementos_de_lista(lista, divisor):
    try:
        return [i/ divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista
    

lista = list(range(10))
divisor = 0
print(divide_elementos_de_lista(lista, divisor))