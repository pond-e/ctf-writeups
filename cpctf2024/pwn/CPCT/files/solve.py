from pwn import *
from struct import pack
import time
io = remote('cpct.web.cpctf.space', 30006)
time.sleep(0.5)
payload = b'a'*4
io.sendlineafter(b'Please enter some string! (max 4 character)\n', payload)
print(io.recv(1024))
