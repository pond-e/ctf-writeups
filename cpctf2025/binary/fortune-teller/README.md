# Fortune Teller

初手 Ghidra でデコンパイルすると複雑そうな処理が並んでたので ChatGPT に解説してもらうと 0x402010 から 0x2d 分のデータを種にフラグの文字列を生成していることが分かった。

そして、その文字と入力文字が一致すれば Correct! が表示されるらしく、 0x402010 からのデータを使ってフラグを構成しようとしたけど上手くいかず、どうせ比較するなら gdb を使って比較直前のレジスタの内容を見れば分かるんじゃと思って動的解析するとフラグが書いてあった。


```
$ gdb -q ./chall
pwndbg: loaded 177 pwndbg commands and 47 shell commands. Type pwndbg [--shell | --all] [filter] for a list.
pwndbg: created $rebase, $base, $hex2ptr, $argv, $envp, $argc, $environ, $bn_sym, $bn_var, $bn_eval, $ida GDB functions (can be used with print/break)
Reading symbols from ./chall...
(No debugging symbols found in ./chall)
------- tip of the day (disable with set show-tips off) -------
Calling functions like call (void)puts("hello world") will run all other target threads for the time the function runs. Use set scheduler-locking on to lock the execution to current thread when calling functions
pwndbg> break *0x4014be
Breakpoint 1 at 0x4014be
pwndbg> run
Starting program: /home/pond/ctf/cpctf2025/binary/fortune-teller/files/chall 

This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.ubuntu.com>
Debuginfod has been disabled.
To make this setting permanent, add 'set debuginfod enabled off' to .gdbinit.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Hi! I'm a fourtune teller. If you want to know your fortune, enter the correct flag.
Input flag: 
Breakpoint 1, 0x00000000004014be in main ()
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
──────────────────────────────────────────────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]───────────────────────────────────────────────────────────────────────────────
 RAX  0
 RBX  0x7fffffffd220 ◂— 0
 RCX  0
 RDX  0
 RDI  0x4020d1 ◂— 0x6f72570073353425 /* '%45s' */
 RSI  0x7fffffffd220 ◂— 0
 R8   0xc
 R9   0x7ffff7fca380 (_dl_fini) ◂— endbr64 
 R10  0x7ffff7db6aa8 ◂— 0x11001200004c7b /* '{L' */
 R11  0x202
 R12  0xffffffff
 R13  2
 R14  0x7fffffffd1f0 ◂— 'CPCTF{y0u_c4n_s01v3_w1th0ut_r3Ad1nG_4ssembly}'
 R15  0x2d
 RBP  0x2d
 RSP  0x7fffffffd0f0 ◂— 0
 RIP  0x4014be (main+782) ◂— call __isoc99_scanf@plt
───────────────────────────────────────────────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]────────────────────────────────────────────────────────────────────────────────────────
 ► 0x4014be <main+782>    call   __isoc99_scanf@plt          <__isoc99_scanf@plt>
        format: 0x4020d1 ◂— 0x6f72570073353425 /* '%45s' */
        vararg: 0x7fffffffd220 ◂— 0
 
   0x4014c3 <main+787>    mov    rdi, r14
   0x4014c6 <main+790>    mov    rsi, rbx
   0x4014c9 <main+793>    call   strcmp@plt                  <strcmp@plt>
 
   0x4014ce <main+798>    test   eax, eax
   0x4014d0 <main+800>    mov    eax, 0x784292c3     EAX => 0x784292c3
   0x4014d5 <main+805>    mov    ecx, 0xb1cda245     ECX => 0xb1cda245
   0x4014da <main+810>    jmp    main+895                    <main+895>
    ↓
   0x40152f <main+895>    cmove  eax, ecx
   0x401532 <main+898>    cmp    eax, 0xd1756cc3
   0x401537 <main+903>    jg     main+187                    <main+187>
─────────────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]─────────────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ rsp 0x7fffffffd0f0 ◂— 0
01:0008│     0x7fffffffd0f8 ◂— 0x2d00000000
02:0010│     0x7fffffffd100 ◂— 0x2dffffffff
03:0018│     0x7fffffffd108 —▸ 0x7fffffffd1e0 ◂— 0x7d /* '}' */
04:0020│     0x7fffffffd110 ◂— 0x5f00000000
05:0028│     0x7fffffffd118 —▸ 0x7fffffffd130 ◂— 0x5000000043 /* 'C' */
06:0030│     0x7fffffffd120 —▸ 0x7fffffffd1f0 ◂— 'CPCTF{y0u_c4n_s01v3_w1th0ut_r3Ad1nG_4ssembly}'
07:0038│     0x7fffffffd128 —▸ 0x7fffffffd220 ◂— 0
───────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]───────────────────────────────────────────────────────────────────────────────────────────────────
 ► 0         0x4014be main+782
   1   0x7ffff7dc81ca __libc_start_call_main+122
   2   0x7ffff7dc828b __libc_start_main+139
   3         0x4010be _start+46
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> 

```
