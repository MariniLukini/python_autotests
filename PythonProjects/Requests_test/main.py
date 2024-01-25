"""
Kolorado test API
"""
import requests

URL = 'https://api.pokemonbattle.me:9104/'
HEADER = {'Content-Type': 'application/json', 'trainer_token': 'bbc8702f55981939817839219569065c'}

# body = {
#    "name": "МарИИнка",
#  "photo": "https://dolnikov.ru/pokemons/albums/930.png"
#}

# body = {
#    "pokemon_id": "28552",
#   "name": "Чудинка",
#  "photo": "https://dolnikov.ru/pokemons/albums/931.png"
#}

body = {
    "pokemon_id": "28552"
}

# response = requests.post (url=f'{URL}/pokemons', json=body, headers=HEADER)
# print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

#response = requests.put (url=f'{URL}/pokemons', json=body, headers=HEADER)
#print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

response = requests.post (url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')