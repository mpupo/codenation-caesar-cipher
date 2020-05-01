import pytest
from my_cesar_crypto import CesarCryptography


@pytest.fixture
def cesar():
    cesar = CesarCryptography()
    return cesar

# @pytest.mark.parametrize("session_id,text",[('1','alô'),('2','alô'),('3','alô')])


def test_example_string(cesar):
    test_message = "d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr"
    message = cesar.decrypt(
        encrypted_message=test_message, backward_steps=3)

    assert message == 'a ligeira raposa marrom saltou sobre o cachorro cansado'


def test_example_string_with_number(cesar):
    test_message = '1a.a'
    encrypted_message = cesar.encrypt(message=test_message, forward_steps=3)

    assert encrypted_message == '1d.d'
