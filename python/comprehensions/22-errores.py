#print(0/0)
#print(var)
print("Hola")
y=0
suma=lambda x, y: x+(y)
#assert y!=0, "y es cero"
#assert es una palabra reservada que nos permite hacer pruebas de forma sencilla
assert suma(1, 2)==3, "La suma no es correcta"

x=10
if x<18:
    raise Exception("x no puede ser mayor que 5")