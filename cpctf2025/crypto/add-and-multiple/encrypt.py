plaintext = input()
a = [ord(i) for i in plaintext]
cipher = 0
for i,chr in enumerate(a,1000):
    cipher += chr
    cipher *= i
f = open('cipher.txt', 'w')
f.write(str(cipher))
f.close()