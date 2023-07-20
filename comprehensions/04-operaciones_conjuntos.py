#Union
planetas={"Marte", "Jupiter", "Venus"}
planetas2={"Tierra","Mercurio","Saturno","Urano","Neptuno"}
planetas3=planetas.union(planetas2)
print(planetas3)
print(planetas|planetas2)

#Intersección
planetas={"Marte", "Jupiter", "Venus"}
planetas2={"Tierra","Mercurio","Saturno","Urano","Neptuno","Marte"}
planetas3=planetas.intersection(planetas2)
print(planetas3)
print(planetas&planetas2)

#Diferencia Esta no es conmutativa
planetas={"Marte", "Jupiter", "Venus"}
planetas2={"Tierra","Mercurio","Saturno","Urano","Neptuno","Marte"}
planetas3=planetas.difference(planetas2)
print(planetas3)
print(planetas-planetas2)
print(planetas2-planetas)

#Diferencia simétrica
planetas={"Marte", "Jupiter", "Venus"}
planetas2={"Tierra","Mercurio","Saturno","Urano","Neptuno","Marte"}
planetas3=planetas.symmetric_difference(planetas2)
print(planetas3)
print(planetas^planetas2)

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
new_set=countries.union(northAm).union(centralAm).union(southAm)

print(new_set)
