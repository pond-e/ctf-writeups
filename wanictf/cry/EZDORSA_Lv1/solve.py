p = 3
q = 5
n = p*q
e = 65535

def gcd2(m, n):
    while n:
        m, n = n, m % n
    return m

l = gcd2((p-1), (q-1))
print("l={}".format(l))
d = pow(e, -1, ((p-1)*(q-1)))
print("d={}".format(d))
M = pow(10, d, n)

print(M)

