from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# Generate a random key (256 bits for AES-256)
key = get_random_bytes(32)

# Data to encrypt
data = "This is a secret message".encode('utf-8')

# Encrypt
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
iv = cipher.iv
encrypted_data = base64.b64encode(iv + ct_bytes).decode('utf-8')

print(f"Encrypted: {encrypted_data}")

# Decrypt
encrypted_data = base64.b64decode(encrypted_data)
iv = encrypted_data[:16]
ct = encrypted_data[16:]
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)
print(f"Decrypted: {pt.decode('utf-8')}")
