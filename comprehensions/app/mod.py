def  get_population():
    keys = ['col', 'df', 'mx']
    values = [300,210,1250]

    return keys, values
a='hello'

def population_by_country(data,country):
    result=list(filter(lambda x:x['Country']==country,data))
    return result


