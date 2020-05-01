"""Código feito para o desafio da Codenation

Criptografia de César"""
import json
import requests

CODENATION_START_CHALLENGE_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
MY_TOKEN = '11ff04314da6eaf77a2f5a853fab2c97a1bd3c9d'

payload = {'token': MY_TOKEN}
start_req = requests.get(CODENATION_START_CHALLENGE_URL, params=payload)

with open('answer.json', 'w') as json_file:
    challenge_params = start_req.json()
    json.dump(challenge_params, json_file)



