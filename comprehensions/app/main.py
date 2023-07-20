import mod 

data=[
        {
            "Country": "Colombia",
            "Population": 500
        },
        {
            "Country": "Mexico",
            "Population": 100
        },
    ]
def run():

    keys,values=mod.get_population()

    print(keys)
    print(values)
    print(mod.a)

    

    country=input("Ingrese el pais a buscar: ")
    result=mod.population_by_country(data,country)
    print(result)

if __name__ == '__main__':
    run()