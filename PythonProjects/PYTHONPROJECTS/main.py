import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e6d606f578369ded9d1c207cf8703a40'
HEADER = {'trainer_token':TOKEN, 'Content-Type':'application/json'}
body_newpokemon = {
    "name": "generate",
    "photo_id": -1
}
body_namepokemon = {
    "pokemon_id": "302133",
    "name": "GoodgameVP",
    "photo_id": 2
}
body_pokeball = {
    "pokemon_id": "302133",
}

response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_newpokemon)
print(response.text)

response_nname = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_namepokemon)
print(response_nname.text)

response_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(response_pokeball.text)