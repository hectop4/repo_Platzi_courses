import utils as utl
import matplotlib.pyplot as plt
import read_csv as rc 
import charts



def run():
    data=rc.read_csv('./APP/data.csv')
    country=input('Ingresa el nombre de un pais: ')
    result=utl.population_by_country(data,country)
    if len(result)>0:
        country=result[0]
        key,value=utl.get_population(data[0])
        charts.generate_bar_chart(key, value)
        #generate_pie_chart(labels, values)

if __name__ == '__main__':
    run()