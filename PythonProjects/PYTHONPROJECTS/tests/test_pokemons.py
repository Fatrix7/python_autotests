import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e6d606f578369ded9d1c207cf8703a40'
HEADER = {'trainer_token':TOKEN, 'Content-Type':'application/json'}
TRAINER_ID = '29189'

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_name():
    response_get = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'frigibax'