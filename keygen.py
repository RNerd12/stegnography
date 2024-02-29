import os

key = os.urandom(32)
iv = os.urandom(16)

with open('key.bin', 'wb') as key_file:
    key_file.write(key)
with open('iv.bin', 'wb') as iv_file:
    iv_file.write(iv)