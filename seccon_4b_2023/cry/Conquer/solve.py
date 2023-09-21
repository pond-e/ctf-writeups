from Crypto.Util.number import *

key = 364765105385226228888267246885507128079813677318333502635464281930855331056070734926401965510936356014326979260977790597194503012948
cipher = 92499232109251162138344223189844914420326826743556872876639400853892198641955596900058352490329330224967987380962193017044830636379

def r_ROL(bits, N):
    for _ in range(N):
        bits = (bits >> 1) | ((bits&1) << (length-1))
    return bits

flag = cipher ^ key
length = key.bit_length()+1
print(length)

for i in range(32):
    key = r_ROL(key, pow(flag, 3, length))
    flag ^= key

flag = long_to_bytes(flag)
print(flag)
