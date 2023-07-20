# Los conjuntos agrupan elementos que tienen algo en común, pero no tienen orden ni índice
# Los conjuntos no pueden tener elementos repetidos
# Los conjuntos son mutables
# Los conjuntos no tienen orden, por lo que no se puede acceder a sus elementos por índice
# Los conjuntos no son indexables
# Los conjuntos no son iterables

set_countries={"Colombia","Perú","Argentina","Chile","Venezuela","Ecuador","Bolivia","Paraguay","Uruguay"}
print(set_countries)
print(type(set_countries))
set_numbers={1,2,3,4,5,6,7,8,9,10}
print(set_numbers)

set_types={1,"Colombia", True ,3.1416,False}
print(set_types)

set_from_string=set("Hello World")
print(set_from_string)

set_from_tuple=set((1,2,3,4,5,6,7,8,9,10,2))
print(set_from_tuple)

set_from_list=set([1,2,3,4,5,6,7,8,9,10,2])
print(set_from_list)
result= list(set_from_list)
print(result)