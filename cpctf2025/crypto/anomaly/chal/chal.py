from Crypto.Util.number import getPrime, bytes_to_long

flag = "CPCTF{fake_flag}"

p = getPrime(512)
e = getPrime(512)
q = 0x10001
n = p * q
c = pow(bytes_to_long(flag.encode()), e, n)

with open("output.py", "w") as f:
    f.write(f"e = {e}\n")
    f.write(f"n = {n}\n")
    f.write(f"c = {c}\n")