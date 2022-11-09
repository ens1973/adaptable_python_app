from os import getenv
from cryptography.fernet import Fernet


def key_generate():
    # generate key
    key=getenv('URL')
    key = key.encode()
    f = Fernet(key)
    return f

def decode_data(data):
    f = key_generate()
    token = f.decrypt(data.encode())
    token = token.decode()
    return token

def encode_data(data):
    f = key_generate()
    token = f.encrypt(data.encode())
    token = token.decode()
    return token