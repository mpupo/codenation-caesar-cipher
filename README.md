# 1. Codenation Python Challenge: Caesar's Cipher

- [1. Codenation Python Challenge: Caesar's Cipher](#1-codenation-python-challenge-caesars-cipher)
- [2. Introduction](#2-introduction)
- [3. The challenge](#3-the-challenge)
  - [3.1. Steps](#31-steps)
    - [3.1.1. Step One: Save the JSON in a file](#311-step-one-save-the-json-in-a-file)
    - [3.1.2. Step Two: Decrypt the text](#312-step-two-decrypt-the-text)
    - [3.1.3. Make a hash code from the decrypted text](#313-make-a-hash-code-from-the-decrypted-text)
    - [3.1.4. Send via POST to Codenation API](#314-send-via-post-to-codenation-api)
- [4. Result](#4-result)

# 2. Introduction


Completing the challenge with a minimum score of 100 points allows the candidate to participate in the selection of the online course "Acelera Dev - Python", sponsored by **Stone**. The course covers Python topics, from beginner to advanced, going from basic language to deploying a complete web application project. Students are evaluated by criteria such as: proficiency in the code, contribution to the course community, commitment to classes, concern with the state and organization of the written code and cooperation with other students.


# 3. The challenge


Write a program, in any programming languagem, that makes a HTTP GET request to the url below:
><https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=YOUR_TOKEN>

The result of request will be a JSON like this:

```JSON
{
	"numero_casas": 10,
	"token":"user_token",
	"cifrado": "encrypted text",
	"decifrado": "decrypted text",
	"resumo_criptografico": "hash code"
}
```

## 3.1. Steps

---

### 3.1.1. Step One: Save the JSON in a file

---

The first step is to save the content of the previous request inside an JSON file named **answer.json**.

### 3.1.2. Step Two: Decrypt the text

---

You might use the number of places (*numero_casas* in JSON) to decrypt the text and update the JSON file in the **decifrado** field.

### 3.1.3. Make a hash code from the decrypted text

---

Use the decrypted text to make a hash code with the SHA1 algorithm (with any programming language) and update the JSON file again.

### 3.1.4. Send via POST to Codenation API

---

Your program should submit via POST the updated JSON file to this url:
><https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=YOUR_TOKEN>

OBS: The API expects a file to be sent as *multipart/form-data*, as if it were sent by an HTML form, with a field of type file  with the name **answer**. Consider this when uploading the file.

# 4. Result

This challenge allowed me to enter the "Acelera Dev - Python" classroom as a "spectator" with the same responsibilities as a regular student (including the same tasks and scores being evaluated), but monitored by other companies that have a partnership with Codenation.
