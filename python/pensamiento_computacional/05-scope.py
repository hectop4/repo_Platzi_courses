#Es el contexto que le pertence a una variable en un programa
#Primero leera las variables globales, luego las funciones, luego las variables locales
#Se crean diferentes contextos para cada funcion donde las variables locales son las que se crean dentro de la funcion
#Las variables globales son las que se crean fuera de las funciones

#Ejemplo de variable global
variable_global = "Esta es una variable global"

def funcion():
    print(variable_global)

funcion()

#Ejemplo de variable local
def funcion2():
    variable_local = "Esta es una variable local"
    print(variable_local)

funcion2()

