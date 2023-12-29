import utils as utl
import matplotlib.pyplot as plt
import read_csv as rc 
import charts
import pandas as pd



def run():

    df=pd.read_csv('./data.csv')
    df=df[df['Continent']=='Africa']
    countries=df['Country/Territory'].values
    percentages=df['World Population Percentage'].values
    charts.generate_pie_chart(countries,percentages)
    print (countries)

    data=rc.read_csv('./data.csv')
    country=input('Ingresa el nombre de un pais: ')
    result=utl.population_by_country(data,country)
    if len(result)>0:
        country=result[0]
        key,value=utl.get_population(data[0])
        charts.generate_bar_chart(country['Country/Territory'],key, value)
        #generate_pie_chart(labels, values)

if __name__ == '__main__':
    run()