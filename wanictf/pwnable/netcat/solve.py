from pwn import *
import time
io = remote('netcat-pwn.wanictf.org', 9001)
# print(io.recv(1024).decode())
for i in range(100):
    time.sleep(0.5)
    x = io.recv(1024)
    print(x)
    x = x.decode()
    if ('Congrats!' in x):
        break
    plus_index = x.rfind('+')
    first = x[plus_index-4:plus_index-1]
    second = x[plus_index+2:plus_index+5]
    io.send('{}\n'.format(int(first) + int(second)))

io.send('cat FLAG\n'.encode())
print(io.recv(1024))


