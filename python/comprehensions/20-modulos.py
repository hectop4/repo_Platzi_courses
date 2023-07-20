# Los modulos en python son archivos con extensión .py que contienen código python
# Estos nos ayudan a organizar nuestro código

import sys

print(sys.path)

#Para importar un módulo, debemos usar la palabra reservada import

import re

#Estas son expresiones regulares que nos ayudan a validar cadenas de texto

text="Hola, mi nombre es Juan, mi numero es 123456789 y mi correo es "

result_text=re.findall('[0-9]+',text)
result=re.findall("Juan",text)
print(result)
print(result_text)

import time

timestamp=time.time()
local=time.localtime(timestamp)
print(timestamp)
print(time.asctime(local))

import collections

#Las colecciones son estructuras de datos que nos ayudan a 
#almacenar datos de una manera más eficiente

numbers=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,"Hola","Hola","Hola","Hola","Hola"]
counter=collections.Counter(numbers)
print(counter)
