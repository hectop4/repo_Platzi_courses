#Filter es una función que recibe una función y una lista. 
#La función que recibe filter devuelve un booleano.
#Si la función devuelve True, el elemento se agrega a la lista resultante.
#Si la función devuelve False, el elemento no se agrega a la lista resultante.

numbers=[1,2,3,4,5,6,7,8,9,10]

new_numbers=list(filter(lambda number: number%2==0,numbers))
print(new_numbers)
print(numbers)

#Filtro De diccionarios

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches)
print("*************"*15)

new_list=list(filter(lambda match: match['home_team_result']=='Win',matches))
print(new_list)
