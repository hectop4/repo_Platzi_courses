#Con try podemos capturar excepciones, con except podemos 
#definir el tipo de excepción a capturar
#para evitar que el programa se detenga
try:
    print(0/0)
    assert 1!=1, "Uno no es igual a uno"
    age=10
    if age<18:
        raise Exception("La edad no puede ser menor que 18")
except ZeroDivisionError as error:
    print(error)
    print("No se puede dividir por cero")
except AssertionError as error:
    print(error)
    print("No se cumple la condición")
except Exception as error:
    print(error)
    print("La edad no puede ser menor que 18")


print('Hola')