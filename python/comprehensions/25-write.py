#r+ read and write mode pero no altera el contenido del archivo
# w+ write and read mode, si el archivo no existe lo crea, si existe lo sobreescribe por completo


with open("./file.txt","w+") as file:
    for line in file:
        print(line, end="")
    file.write("\nHola")