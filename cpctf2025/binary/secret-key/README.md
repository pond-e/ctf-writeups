# Secret Key
いつもの rev 問題って感じ

Ghidraで解析すると比較に使ってる文字が 1 文字ずつ見える

ここの if 文は入力された文字の順番と、ここに並んでる文字の順番が全然違うことに注意する必要がある

本当の順番は最初の変数宣言の順番になっていて、「reversing」を入力するとフラグをゲットできる


```

undefined8 main(void)

{
  long in_FS_OFFSET;
  char local_1a;
  char local_19;
  char local_18;
  char local_17;
  char local_16;
  char local_15;
  char local_14;
  char local_13;
  char local_12;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Too see flag, you need Secret Key. Please enter it:");
  __isoc99_scanf(&DAT_0010204c,&local_1a);
  if ((((((local_12 == 'g') && (local_1a == 'r')) && (local_14 == 'i')) &&
       ((local_15 == 's' && (local_17 == 'e')))) &&
      ((local_13 == 'n' && ((local_18 == 'v' && (local_16 == 'r')))))) && (local_19 == 'e')) {
    puts("Congraturations!");
    printflag();
  }
  else {
    puts("Wrong Key!");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}


```

```
$ ./chall 
Too see flag, you need Secret Key. Please enter it:reversing
Congraturations!
Flag: CPCTF{h4PPy_b1n4ry_h4ck1nG!}
```
