countries=['Finland','Sweden','Norway','Denmark','Iceland']
populations=[5.5,10.0,5.7,3.7,0.4]


population_v2={countries[i]:populations[i] for i in range(len(countries)) if populations[i]>5}
print(population_v2)

text='I am enjoying this challenge.\nI just wonder what is next.'

unique={i:text.count(i) for i in text if i!='\n' and i!=' '}
print(unique)