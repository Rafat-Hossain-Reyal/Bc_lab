import os
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

# Generate RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Encrypt private key with password using AES
password = input("Enter password: ")
salt = os.urandom(16)
key_derived = PBKDF2(password, salt, dkLen=32, count=100_000)
cipher_aes = AES.new(key_derived, AES.MODE_CBC)
ct_bytes = cipher_aes.encrypt(pad(private_key, AES.block_size))

with open('private_key.enc', 'wb') as f:
    f.write(salt + cipher_aes.iv + ct_bytes)

# Decrypt private key
with open('private_key.enc', 'rb') as f:
    file_data = f.read()
    salt, iv, ciphertext = file_data[:16], file_data[16:32], file_data[32:]

key_derived = PBKDF2(password, salt, dkLen=32, count=100_000)
cipher_aes = AES.new(key_derived, AES.MODE_CBC, iv)
decrypted_private_key = unpad(cipher_aes.decrypt(ciphertext), AES.block_size)
restored_key = RSA.import_key(decrypted_private_key)

# Sign message
message = "Hello, world!"
hash_message = SHA256.new(message.encode())
signature = pkcs1_15.new(restored_key).sign(hash_message)

# Verify signature
try:
    pkcs1_15.new(restored_key.publickey()).verify(hash_message, signature)
    print("Signature is valid")
except (ValueError, TypeError):
    print("Signature is invalid")
