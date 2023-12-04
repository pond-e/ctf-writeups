headerが
`00000000  00 00 00 e0 00 10 4a 46  49 46 00 01 01 00 00 01  |......JFIF......|`
となっている
1. ghexでheaderを直接かく

2. 
```bash
$ sudo gunzip /usr/share/wordlists/rockyou.txt.gz
$ stegseek layers_after.jpg
$ cat layers_after.jpg.out
```
