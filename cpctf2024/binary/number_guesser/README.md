# number guesser
ghidraで開けば答えが書いてある
```c

undefined8 main(void)

{
  long in_FS_OFFSET;
  undefined8 local_1a;
  undefined2 local_12;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_1a = 0;
  local_12 = 0;
  puts("Guess the number!");
  __isoc99_scanf(&DAT_00102016,&local_1a);
  if (((((char)local_1a == '1') && (local_1a._1_1_ == '7')) && (local_1a._2_1_ == '7')) &&
     (((local_1a._3_1_ == '0' && (local_1a._4_1_ == '4')) && (local_1a._5_1_ == '\0')))) {
    printFlag(&local_1a);
  }
  else {
    puts("Wrong...");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

```
17704でフラグが出てくる
`CPCTF{l4Ck3Y_NuMb3R!}`