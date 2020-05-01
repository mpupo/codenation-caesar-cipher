"""Implementação do algorítmo de criptografia de César do desafio. """


class CesarCryptography(object):
    _letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
    _punctuation = [',', '.', ';']

    def decrypt(self, encrypted_message: str, backward_steps: int = 1) -> str:
        encrypted_message = encrypted_message.lower()
        encrypted_phrases = encrypted_message.split()
        decoded_words = []
        for phrase in encrypted_phrases:
            decoded_letters = []
            for letter in phrase:

                if letter.isnumeric():
                    decoded_letters.append(letter)
                    continue
                elif letter in self._punctuation:
                    decoded_letters.append(letter)
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

                decoded_letters.append(letter_decrypted)
            word = ''.join(decoded_letters)
            decoded_words.append(word)

        decoded_message = ' '.join(decoded_words)

        return decoded_message

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
