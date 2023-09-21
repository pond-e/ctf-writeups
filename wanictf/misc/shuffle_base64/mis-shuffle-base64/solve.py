import base64
cipher = b'fWQobGVxRkxUZmZ8NjQsaHUhe3NAQUch'
cipher_base64_de = base64.b64decode(cipher)
print(cipher_base64_de)
print(cipher_base64_de.decode())
