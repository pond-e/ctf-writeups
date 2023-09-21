import math
cipher = [4396, 22819, 47998, 47995, 40007, 9235, 21625, 25006, 4397, 51534, 46680, 44129, 38055, 18513, 24368, 38451, 46240, 20758, 37257, 40830, 25293, 38845, 22503, 44535, 22210, 39632, 38046, 43687, 48413, 47525, 23718, 51567, 23115, 42461, 26272, 28933, 23726, 48845, 21924, 46225, 20488, 27579, 21636]

index = []
for i in cipher:
    for j in range(49):
        if math.sqrt((i-j)) % 1 == 0:
#            print("Yes")
            index.append(j)

tmp = cipher.copy()
count = 0
for i in index:
    tmp[i] = int(math.sqrt(cipher[count] - i))
    count += 1

hoge = ord('c')
print('c', end='')
for i in tmp:
    print(chr(i-hoge), end='')
    #print(i-hoge+base)
    hoge = i-hoge
    
