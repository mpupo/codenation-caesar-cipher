"""Code made for the Codenation challenge "Caesar's Cryptography" """
import json
import requests

CODENATION_START_CHALLENGE_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
MY_TOKEN = 'MY_SECRET_TOKEN'

payload = {'token': MY_TOKEN}
start_req = requests.get(CODENATION_START_CHALLENGE_URL, params=payload)

with open('answer_original.json', 'w') as json_file:
    challenge_params = start_req.json()
    json.dump(challenge_params, json_file)
