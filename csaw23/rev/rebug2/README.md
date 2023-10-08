# rebug2
ghidraでmain関数を見てみる
```C
undefined8 main(void)

{
  undefined8 local_28;
  undefined8 local_20;
  undefined4 local_18;
  int local_10;
  uint local_c;
  
  local_28 = 0x6e37625970416742;
  local_20 = 0x44777343;
  local_18 = 0;
  local_10 = 0xc;
  printf("That is incorrect :(");
  for (local_c = 0; (int)local_c < local_10; local_c = local_c + 1) {
    if (((local_c & 1) == 0) && (local_c != 0)) {
      printbinchar((int)*(char *)((long)&local_28 + (long)(int)local_c));
    }
  }
  return 0;
}
```

for文が0xc回呼ばれてるのと、偶数回の時にprintbinchar関数が呼ばれてるのが分かる
```C
void printbinchar(char param_1)

{
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  uint local_14;
  char local_d;
  int local_c;
  
  local_38 = 0;
  local_30 = 0;
  local_28 = 0;
  local_20 = 0;
  for (local_c = 0; local_c < 8; local_c = local_c + 1) {
    local_14 = ((int)param_1 << ((byte)local_c & 0x1f)) >> 7 & 1;
    *(uint *)((long)&local_38 + (long)local_c * 4) = local_14;
  }
  local_d = param_1;
  xoring(&local_38);
  return;
}
```

for文が8回よばれて、何か色々計算してる

最後にxoring関数が呼ばれている
```C
undefined8 xoring(long param_1)

{
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  int local_10;
  int local_c;
  
  local_28 = 0;
  local_20 = 0;
  local_38 = 0;
  local_30 = 0;
  for (local_c = 0; local_c < 4; local_c = local_c + 1) {
    *(undefined4 *)((long)&local_28 + (long)local_c * 4) =
         *(undefined4 *)(param_1 + (long)local_c * 4);
    *(undefined4 *)((long)&local_38 + (long)local_c * 4) =
         *(undefined4 *)(param_1 + ((long)local_c + 4) * 4);
  }
  for (local_10 = 0; local_10 < 4; local_10 = local_10 + 1) {
    if (*(int *)((long)&local_28 + (long)local_10 * 4) ==
        *(int *)((long)&local_38 + (long)local_10 * 4)) {
      flag[index_flag] = 0x30;
    }
    else {
      flag[index_flag] = 0x31;
    }
    index_flag = index_flag + 1;
  }
  return 0;
}
```

始め引数を2つのローカル配列にコピーをして、4回ループしている

もし、両方配列のあるインデックスの値が等しければflag[index_flag]に0を、そうでないなら1を入れている

その後flag_indexをインクリメントしている

flagがこの中で宣言されてないのに使われてるからグローバル変数かもしれない

一連の動作を再現するためにgdbを使って動的解析をしてみる
```bash
$ gdb ./bin.out
GNU gdb (Debian 13.2-1) 13.2
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./bin.out...
(No debugging symbols found in ./bin.out)
gdb-peda$ starti
Starting program: /home/kali/ctf/csaw23/rev/rebug2/bin.out 

Program stopped.
Warning: 'set logging off', an alias for the command 'set logging enabled', is deprecated.
Use 'set logging enabled off'.

Warning: 'set logging on', an alias for the command 'set logging enabled', is deprecated.
Use 'set logging enabled on'.


[----------------------------------registers-----------------------------------]
RAX: 0x0 
RBX: 0x0 
RCX: 0x0 
RDX: 0x0 
RSI: 0x0 
RDI: 0x0 
RBP: 0x0 
RSP: 0x7fffffffddb0 --> 0x1 
RIP: 0x7ffff7fe5220 (<_start>:	mov    rdi,rsp)
R8 : 0x0 
R9 : 0x0 
R10: 0x0 
R11: 0x0 
R12: 0x0 
R13: 0x0 
R14: 0x0 
R15: 0x0
EFLAGS: 0x200 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x7ffff7fe520c <_dl_help+668>:	jmp    0x7ffff7fe4fa0 <_dl_help+48>
   0x7ffff7fe5211:	cs nop WORD PTR [rax+rax*1+0x0]
   0x7ffff7fe521b:	nop    DWORD PTR [rax+rax*1+0x0]
=> 0x7ffff7fe5220 <_start>:	mov    rdi,rsp
   0x7ffff7fe5223 <_start+3>:	call   0x7ffff7fe5e00 <_dl_start>
   0x7ffff7fe5228 <_dl_start_user>:	mov    r12,rax
   0x7ffff7fe522b <_dl_start_user+3>:	mov    rdx,QWORD PTR [rsp]
   0x7ffff7fe522f <_dl_start_user+7>:	mov    rsi,rdx
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffddb0 --> 0x1 
0008| 0x7fffffffddb8 --> 0x7fffffffe15e ("/home/kali/ctf/csaw23/rev/rebug2/bin.out")
0016| 0x7fffffffddc0 --> 0x0 
0024| 0x7fffffffddc8 --> 0x7fffffffe187 ("TERMINATOR_DBUS_NAME=net.tenshu.Terminator21a9d5db22c73a993ff0b42f64b396873")
0032| 0x7fffffffddd0 --> 0x7fffffffe1d3 ("SSH_AUTH_SOCK=/tmp/ssh-kxiudYsNPTp9/agent.991")
0040| 0x7fffffffddd8 --> 0x7fffffffe201 ("SESSION_MANAGER=local/kali:@/tmp/.ICE-unix/991,unix/kali:/tmp/.ICE-unix/991")
0048| 0x7fffffffdde0 --> 0x7fffffffe24d ("SSH_AGENT_PID=1114")
0056| 0x7fffffffdde8 --> 0x7fffffffe260 ("LANG=en_US.UTF-8")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x00007ffff7fe5220 in _start () from /lib64/ld-linux-x86-64.so.2
gdb-peda$ disassemble main
Dump of assembler code for function main:
   0x00005555555552a4 <+0>:	push   rbp
   0x00005555555552a5 <+1>:	mov    rbp,rsp
   0x00005555555552a8 <+4>:	sub    rsp,0x20
   0x00005555555552ac <+8>:	movabs rax,0x6e37625970416742
   0x00005555555552b6 <+18>:	mov    edx,0x44777343
   0x00005555555552bb <+23>:	mov    QWORD PTR [rbp-0x20],rax
   0x00005555555552bf <+27>:	mov    QWORD PTR [rbp-0x18],rdx
   0x00005555555552c3 <+31>:	mov    DWORD PTR [rbp-0x10],0x0
   0x00005555555552ca <+38>:	mov    DWORD PTR [rbp-0x8],0xc
   0x00005555555552d1 <+45>:	lea    rax,[rip+0xd2c]        # 0x555555556004
   0x00005555555552d8 <+52>:	mov    rdi,rax
   0x00005555555552db <+55>:	mov    eax,0x0
   0x00005555555552e0 <+60>:	call   0x555555555030 <printf@plt>
   0x00005555555552e5 <+65>:	mov    DWORD PTR [rbp-0x4],0x0
   0x00005555555552ec <+72>:	jmp    0x555555555316 <main+114>
   0x00005555555552ee <+74>:	mov    eax,DWORD PTR [rbp-0x4]
   0x00005555555552f1 <+77>:	and    eax,0x1
   0x00005555555552f4 <+80>:	test   eax,eax
   0x00005555555552f6 <+82>:	jne    0x555555555312 <main+110>
   0x00005555555552f8 <+84>:	cmp    DWORD PTR [rbp-0x4],0x0
   0x00005555555552fc <+88>:	je     0x555555555312 <main+110>
   0x00005555555552fe <+90>:	mov    eax,DWORD PTR [rbp-0x4]
   0x0000555555555301 <+93>:	cdqe
   0x0000555555555303 <+95>:	movzx  eax,BYTE PTR [rbp+rax*1-0x20]
   0x0000555555555308 <+100>:	movsx  eax,al
   0x000055555555530b <+103>:	mov    edi,eax
   0x000055555555530d <+105>:	call   0x55555555522c <printbinchar>
   0x0000555555555312 <+110>:	add    DWORD PTR [rbp-0x4],0x1
   0x0000555555555316 <+114>:	mov    eax,DWORD PTR [rbp-0x4]
   0x0000555555555319 <+117>:	cmp    eax,DWORD PTR [rbp-0x8]
   0x000055555555531c <+120>:	jl     0x5555555552ee <main+74>
   0x000055555555531e <+122>:	mov    eax,0x0
   0x0000555555555323 <+127>:	leave
   0x0000555555555324 <+128>:	ret
End of assembler dump.
gdb-peda$ break *0x000055555555531e
Breakpoint 1 at 0x55555555531e
```

startiでgdbを始める。startだといけるところまで実行しちゃうからstartiコマンドを使ってelaboration phaseの開始点で実行を停止する（runコマンドと同じ動作）。

mainの終わりギリギリにbreak pointを設定
```bash
gdb-peda$ c
Continuing.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

[----------------------------------registers-----------------------------------]
RAX: 0xc ('\x0c')
RBX: 0x7fffffffddb8 --> 0x7fffffffe15e ("/home/kali/ctf/csaw23/rev/rebug2/bin.out")
RCX: 0x7 
RDX: 0x555555558030 ("01011100010001110000")
RSI: 0x28 ('(')
RDI: 0x7fffffffdc40 --> 0x100000000 
RBP: 0x7fffffffdca0 --> 0x1 
RSP: 0x7fffffffdc80 ("BgApYb7nCswD")
RIP: 0x55555555531e (<main+122>:	mov    eax,0x0)
R8 : 0x400 
R9 : 0x410 
R10: 0x1000 
R11: 0x3f ('?')
R12: 0x0 
R13: 0x7fffffffddc8 --> 0x7fffffffe187 ("TERMINATOR_DBUS_NAME=net.tenshu.Terminator21a9d5db22c73a993ff0b42f64b396873")
R14: 0x555555557dd8 --> 0x5555555550f0 (<__do_global_dtors_aux>:	endbr64)
R15: 0x7ffff7ffd000 --> 0x7ffff7ffe2c0 --> 0x555555554000 --> 0x10102464c457f
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x555555555316 <main+114>:	mov    eax,DWORD PTR [rbp-0x4]
   0x555555555319 <main+117>:	cmp    eax,DWORD PTR [rbp-0x8]
   0x55555555531c <main+120>:	jl     0x5555555552ee <main+74>
=> 0x55555555531e <main+122>:	mov    eax,0x0
   0x555555555323 <main+127>:	leave
   0x555555555324 <main+128>:	ret
   0x555555555325:	add    BYTE PTR [rax],al
   0x555555555327:	add    BYTE PTR [rax-0x7d],cl
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdc80 ("BgApYb7nCswD")
0008| 0x7fffffffdc88 --> 0x44777343 ('CswD')
0016| 0x7fffffffdc90 --> 0x0 
0024| 0x7fffffffdc98 --> 0xc0000000c ('\x0c')
0032| 0x7fffffffdca0 --> 0x1 
0040| 0x7fffffffdca8 --> 0x7ffff7df16ca (<__libc_start_call_main+122>:	mov    edi,eax)
0048| 0x7fffffffdcb0 --> 0x0 
0056| 0x7fffffffdcb8 --> 0x5555555552a4 (<main>:	push   rbp)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x000055555555531e in main ()

```

スタックには入力文字列BgApYb7nCswD（前問でも使った12文字の適当な文字）が入ってるけど、今はグローバル変数flagの中身がみたい（スタックにはない？）

x(inspect)と/s(string)を&flagに対してするとflagが見れる
```bash
gdb-peda$ x/s &flag
0x555555558030 <flag>:	"01011100010001110000"
```
`csawctf{01011100010001110000}`