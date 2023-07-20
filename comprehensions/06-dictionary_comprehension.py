#{key:value for var in iterable}

dict={}
for i in range(1,11):
    dict[i]=i**2
print(dict)

dict_v2={i:i**2 for i in range(1,11)}

countries=['Finland','Sweden','Norway','Denmark','Iceland']
populations=[5.5,10.0,5.7,3.7,0.4]
for i in range(len(countries)):
    dict_v2[countries[i]]=populations[i]
print(dict_v2)

dict_v3={countries[i]:populations[i] for i in range(len(countries))}
print(dict_v3)


names=['Asabeneh','Brook','David','John']
countries=['Finland','Sweden','Norway','Denmark']

dict_v4={names[i]:countries[i] for i in range(len(names))}
print(dict_v4)

new_dict={name:countries for name,countries in zip(names,countries)}
print(new_dict)