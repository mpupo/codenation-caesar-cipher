"""Implementação do algorítmo de criptografia de César do desafio. """


class CesarCryptography(object):
    _letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
    _punctuation = [',', '.', ';']

    def decrypt(self, encrypted_message: str, backward_steps: int = 1) -> str:
        encrypted_message = encrypted_message.lower()
        encrypted_phrases = encrypted_message.split()
        decrypted_words = []
        for phrase in encrypted_phrases:
            decrypted_letters = []
            for letter in phrase:

                if letter.isnumeric():
                    decrypted_letters.append(letter)
                    continue
                elif letter in self._punctuation:
                    decrypted_letters.append(letter)
                    continue
                elif letter == ' ':
                    continue
                elif letter == '':
                    continue
                elif letter.isspace():
                    continue

                index = self._letters.index(letter)
                index_decrypt = index - backward_steps

                letter_decrypted = self._letters[index_decrypt]

                decrypted_letters.append(letter_decrypted)
            word = ''.join(decrypted_letters)
            decrypted_words.append(word)

        decrypted_message = ' '.join(decrypted_words)

        return decrypted_message

    def encrypt(self, message: str, forward_steps: int = 1) -> str:
        message = message.lower()
        message_phrases = message.split()
        encrypted_words = []

        for phrase in message_phrases:
            encrypted_letters = []
            for letter in message:
                if letter.isnumeric():
                    encrypted_letters.append(letter)
                    continue
                elif letter in self._punctuation:
                    encrypted_letters.append(letter)
                    continue
                elif letter == ' ':
                    continue
                elif letter == '':
                    continue
                elif letter.isspace():
                    continue

                index = self._letters.index(letter)
                index_crypt = index + forward_steps

                if index_crypt > len(self._letters):
                    index_crypt = 0 + forward_steps

                letter_encrypted = self._letters[index_crypt]
                encrypted_letters.append(letter_encrypted)

            encrypted_word = ''.join(encrypted_letters)
            encrypted_words.append(encrypted_word)

        encrypted_message = ' '.join(encrypted_words)

        return encrypted_message
