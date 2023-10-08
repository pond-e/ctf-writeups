# rebug1
`test.out`というELFファイルが配布されるのでそれをghidraで開きます
```C
  printf("Enter the String: ");
  __isoc99_scanf(&DAT_00102017,local_408);
  for (local_c = 0; local_408[local_c] != '\0'; local_c = local_c + 1) {
  }
  if (local_c == 0xc) {
    puts("that\'s correct!");
    local_18 = (EVP_MD_CTX *)EVP_MD_CTX_new();
    type = EVP_md5();
    EVP_DigestInit_ex(local_18,type,(ENGINE *)0x0);
    EVP_DigestUpdate(local_18,&DAT_0010202a,2);
    local_41c = 0x10;
    EVP_DigestFinal_ex(local_18,local_418,&local_41c);
    EVP_MD_CTX_free(local_18);
    for (local_10 = 0; local_10 < 0x10; local_10 = local_10 + 1) {
      sprintf(local_448 + local_10 * 2,"%02x",(ulong)local_418[local_10]);
    }
    printf("csawctf{%s}\n",local_448);
  }
  else {
    printf("that isn\'t correct, im sorry!");
  }
```
2行目、local_408に入力した文字が入ります

3行目ではlocal_cにlocal_408の文字数が入ります

C言語では文字列の最後には\0が入る決まりなので、文字列の先頭から\0までループをまわすと、ループを回した回数が文字列の長さになります

local_cが0xcなら「that's correct!」なので入力する文字数を12文字にしたらよさそうです

```bash
$ ./test.out 
Enter the String: jjjjkkkkllll
that's correct!
csawctf{c20ad4d76fe97759aa27a0c99bff6710}
```