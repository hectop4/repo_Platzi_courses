#
def find_volume(length=10,width=20,height=30):
    
    return length * width * height, width * height,"Hola"

result =find_volume(10,29,30)
print(result)
result_2 = find_volume()
print(result_2)
result_3 = find_volume(width=100)
print(result_3)
print(type(result_3))
print(result_3[0])
result ,w,h = find_volume()
print(result,w,h)