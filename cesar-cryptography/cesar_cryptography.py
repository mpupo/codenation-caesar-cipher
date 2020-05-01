"""Implementação do desafio"""

import json
import requests
from my_cesar_crypto import CesarCryptography

CODENATION_START_CHALLENGE_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
MY_TOKEN = '11ff04314da6eaf77a2f5a853fab2c97a1bd3c9d'

payload = {'token': MY_TOKEN}

challenge_answer = {}
cesar = CesarCryptography()

with open('answer_original.json', 'r') as json_file:
    challenge_answer = json.load(json_file)

encrypted = challenge_answer['cifrado']
steps = challenge_answer['numero_casas']
decrypted_challenge_msg = cesar.decrypt(encrypted, steps)
print(decrypted_challenge_msg)
