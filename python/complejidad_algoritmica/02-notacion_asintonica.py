#Big o notation - notacion asintotica 
#Es una forma de medir el rendimiento de un algoritmo, 
#en funcion del crecimiento de los datos
#No importan las variaciones pequenas
#Se mide en tiempo de ejecucion y en espacio en memoria

#Un loop, crecimiento lineal
#un loop dentro de otro loop, crecimiento cuadratico
#llamadas recursivas, crecimiento exponential

def f(n):
    for i in range(n):
        print(i)
    for i in range(n):
        print(i)

#O(n)+O(n) = O(n+n) = O(2n) = O(n)


def f(n):
    for i in range(n):
        print(i)
    for i in range(n*n):
        print(i)

#O(n)+O(n*n) = O(n+n^2) = O(n^2)

#Ley de la multiplicacion

def f2(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
#O(n)*O(n) = O(n*n) = O(n^2)

#Recursividad multiple
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
#O(2^n)


