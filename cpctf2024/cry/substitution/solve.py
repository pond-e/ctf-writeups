moto = ["p", "z", "u", "k", "n", "i", "e", "x", "a", "v", "m", "d", "s", "t", "g", "j", "l", "w", "r", "f", "c", "q", "y", "b"]
saki = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "l", "d", "c", "u", "m", "w", "f", "g", "y", "p", "b", "v", "k", "j", "x", "q", "z"]
input_text = "Cpvv muzp! Xuvdazs ijax ekrtiusknl kpqgakpx fuij xwavv nzm tniapzep. Rug'dp mpluzxiknipm pyeptiauznv neglpz nzm tpkxpdpknzep. Fkndu buk eknewazs ijp eump nzm gzvuewazs aix xpekpix! ETEIB{jpvvu_ekrtiu_cukvm}"
input_text = input_text.lower()
output_text = ""
flag = False
for input_ in input_text:
    for i in range(24):
        if input_ == moto[i]:
            output_text += saki[i]
            flag = True
    if flag == False:
        output_text += input_
    flag = False

print(output_text)
