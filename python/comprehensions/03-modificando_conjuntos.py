#Crud significa crear, leer, actualizar y eliminar
#Crear un conjunto
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

#Longitud de un conjunto
print(len(planetas))
print("Marte" in planetas)

#Agregar elementos a un conjunto
planetas.add("Tierra")
print(planetas)

#Eliminar elementos de un conjunto
planetas.remove("Tierra")
print(planetas)
#planetas.remove("Tierra") #Genera error si el elemento no existe

#Eliminar elementos de un conjunto sin generar error si el elemento no existe
planetas.discard("Tierra")
print(planetas)

#update
planetas.update(["Mercurio","Saturno","Urano","Neptuno"])
print(planetas)
planetas.update({"Pluton","Ceres","Eris"})
print(planetas)



#Limpiar un conjunto
planetas.clear()
print(planetas)

