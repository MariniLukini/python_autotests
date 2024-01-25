import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104/'
HEADER = {'Content-Type': 'application/json', 'trainer_token': 'bbc8702f55981939817839219569065c'}

def test_get_trainers_level():
 """
 Проверка на код 200
 """
 response = requests.get(url=f'{URL}/trainers', params={'level':1}, timeout=5)
 assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_trainer_id():
 """
 Проверка имени тренера
 """
 response = requests.get(url=f'{URL}/trainers', params={'trainer_id':3716}, timeout=5)
 assert response.json()['trainer_name'] == 'LukiniMarini', 'Unexpected trainer name'