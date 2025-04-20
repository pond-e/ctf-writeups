enc = 'CQAWB~v^kVi?bRl? bfLdLb_(wEk/ox/rLcMG@['

for i, b in enumerate(enc):
    print(chr(ord(b)^i), end='')

print()
