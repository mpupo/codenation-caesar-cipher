"""Challenge resolution"""

import json
import requests
import hashlib
from my_cesar_crypto import CesarCryptography

CODENATION_SENDFILE_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?'
MY_TOKEN = 'MY_SECRET_TOKEN'
payload = {'token': MY_TOKEN}

# 1. Retrieving the data:
challenge_answer = {}
with open('answer_original.json', 'r') as json_file:
    challenge_answer = json.load(json_file)

# 2. Decrypting the message:
cesar = CesarCryptography()
encrypted = challenge_answer['cifrado']
steps = challenge_answer['numero_casas']
decrypted_challenge_msg = cesar.decrypt(encrypted, steps)

# 3. Generating the hash of message:
decrypted_msg_hash = hashlib.sha1(decrypted_challenge_msg.encode()).hexdigest()

# 4. Updating the challenge parameters:
challenge_answer['decifrado'] = decrypted_challenge_msg
challenge_answer['resumo_criptografico'] = decrypted_msg_hash

# 5. Generating the answer.json file:
with open('answer.json', 'w') as json_file:
    json.dump(challenge_answer, json_file)

# 6. Send to Codenation:
file = {"answer": open('answer.json', 'rb')}
send = requests.post(url=CODENATION_SENDFILE_URL, params=payload, files=file)

# 7. Saving the Codenation answer response:
with open('codenation_response.json', 'w') as json_file:
    response = send.json()
    json.dump(response, json_file)
