#Sucesion de Fibonacci

def fibonacci(n):
    """Calcula el enesimo valor de la sucesion de Fibonacci
        param int n>0
    """
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input('Escribe un entero: '))
print(fibonacci(n))