with open("flag_enc.txt", "rb") as f:
    ans = ""
    # print(f)
    for text in f:
        for raw in text:
            tmp_mod = raw//16
            tmp_div = (raw - tmp_mod*16)*16
            # print(tmp_mod+tmp_div)
            ans += chr(tmp_mod+tmp_div)
    ans = ans[::-1]
    print(ans)
