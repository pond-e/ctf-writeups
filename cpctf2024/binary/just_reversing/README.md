# just reversing
chall.cとflag_enc.txtが配られる
```c
#include <stdio.h>
#include <string.h>

int main() {
	char flag_enc[30] = "";
	char flag[30];
	FILE *f;
	f = fopen("flag.txt", "r");
	if (f == NULL) {
		printf("flag.txt not found\n");
		return 1;
	}
	fscanf(f, "%s", flag);
	fclose(f);

	for (int i = 0; i < strlen(flag); i++) {
		char chr = flag[i];
		flag_enc[strlen(flag) - i - 1] = chr / 16 + chr % 16 * 16;
	}

	f = fopen("flag_enc.txt", "w");
	fprintf(f, "%s", flag_enc);
	fclose(f);

	return 0;
}
```
chrは高々200ぐらいだから16^2で割れば0になってchr%16だけが残る

pythonでやる場合はopenに"rb"をつけないとエラーになるから注意
```python
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

```