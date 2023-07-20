#Algoritmica, una forma de crear soluciones usando el princio de divide y venceras
#Programatico, una funcion que se llama a si misma

#factorial de un numero

def factorial(n):
    """
    Calcula el factorial de n con n un valor entero
    param int n > 0"""
    if n == 1:
        return 1
    return n * factorial(n-1)

n = int(input('Escribe un entero: '))

print(factorial(n))