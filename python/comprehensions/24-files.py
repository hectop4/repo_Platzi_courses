file = open("./file.txt", "r")
#print(file.read())
#print(file.readline())
#print(file.readline())
#print(file.readline())

for line in file:
    print(line)



file.close()

with open("./file.txt", "r") as file:
    for line in file:
        print(line)