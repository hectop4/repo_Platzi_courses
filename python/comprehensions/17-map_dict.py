items=[
    {
    "product":'camisa',
    "price":5000
    
     },
    {
    "product":'pantalon',
    "price":10000
     },
    {
    "product":'zapatos',
    "price":20000
        },
]
prices=list(map(lambda item: item['price'], items))
print(items)
print(prices)

def add_taxes(item):
    new_item=item.copy()
    #Aqui se modifica el diccionario original
    new_item['taxes']=item['price']*0.19
    return new_item

new_items=list(map(add_taxes, items))
print("Nueva lista")
print(new_items)
#Se modifico la lista original y no queremos eso
#Esto se debe al lugar en memoria donde se almacenan las listas
print("Lista original")
print(items)


