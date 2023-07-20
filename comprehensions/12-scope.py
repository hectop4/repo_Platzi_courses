#------------------------------------>
#Local Scope    Enclosing Scope    Global Scope    Built-in Scope
#------------------------------------>
# 1. Local Scope
#es una variable que se encuentra dentro de una funcion
# 2. Enclosing Scope
#Es una variable que se encuentra dentro de una funcion pero que esta dentro de otra funcion
# 3. Global Scope
#Es una variable que se encuentra fuera de una funcion
# 4. Built-in Scope
#Es una variable que se encuentra en el interprete de python
#------------------------------------>

price=100 #Global Scope
print(price)

def scope():
    
    #price =price + 100 Is an error because price is a local variable
    price=200 #Local Scope
    result = price + 100 # Solo tienen contexto dentro de la funcion
    print(price)
    return price #Solo tienen contexto dentro de la funcion

print(price)
print(scope())
