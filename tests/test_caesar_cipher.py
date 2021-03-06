import pytest
from caesar_cipher.cipher import crack, encrypt, decrypt

def test_encrypt_my_name():
    encrypted_word = encrypt('garfield', 2)
    assert encrypted_word == "icthkgnf"

def test_decrypt():
    encrypted_word = 'icthkgnf'
    actual = decrypt(encrypted_word,2)
    assert actual == 'garfield'

def test_cipher_all_caps():
    encrypted_word = encrypt('BOY', 2)
    actual = crack(encrypted_word)
    expected = 'BOY'
    assert actual == expected
    
    
def test_crack():
    encrypted_word = encrypt("python", 1)
    actual = crack(encrypted_word)
    expected = "python"
    assert actual == expected

def test_decrypt():
    decrypt('bcd', 1)
    assert 'abc'



def test_crack():
    sentence = 'i am a boy'
    encrypted_word = encrypt(sentence, 1)
    # actual = decrypt(encrypted_word, 1)
    actual = crack(encrypted_word)
    expected = sentence
    assert actual == expected


