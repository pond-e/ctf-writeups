cipher = 103200264548574214569124695908951019136986646123214535931636006688814109904122192900997137101
ans = ""
for i in range(1000,1000+100):
    if cipher % i == 0:
        j = i
        while cipher != 0:
            cipher //= j
            print(cipher % (j-1))
            ans += chr(int(cipher % (j-1)))
            cipher -= int(cipher % (j-1))
            j -= 1

print(ans[::-1])
