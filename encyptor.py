from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

with open('key.bin', 'rb') as key_file:
    key = key_file.read()
with open('iv.bin', 'rb') as iv_file:
    iv = iv_file.read()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

def aes_encrypt(plaintext: str):
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder() 
    padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def aes_decrypt(ciphertext: str):
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode('utf-8')

if __name__ == '__main__':
    text = "password"
    print(text)
    crypt_text = aes_encrypt(text)
    print(crypt_text)
    print(bytes([i for i in crypt_text]))