# Guessing

pycファイルって何ぞやってところからスタート

どうやら Python コードをバイトコードにコンパイル？したものらしい（適当な認識ですみません）

このファイルは Python 3.13 で作られたらしく、Python 3.13 にしないと実行できない罠に最初はまった

ChatGPT に pyc ファイルを解析するコードを書いてもらって実行すると、 xor の計算をしてそうなことが分かったので適当にエスパーをするとフラグをゲットできた

```
pond@laptop-8UQA2MI:~/ctf/cpctf2025/binary/guessing/files$ uv venv -p 3.13
Using CPython 3.13.3
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
pond@laptop-8UQA2MI:~/ctf/cpctf2025/binary/guessing/files$ source .venv/bin/activate
(files) pond@laptop-8UQA2MI:~/ctf/cpctf2025/binary/guessing/files$ python --version
Python 3.13.3
(files) pond@laptop-8UQA2MI:~/ctf/cpctf2025/binary/guessing/files$ cat hoge.py 
import marshal, dis
import io, types

# 1) .pyc ヘッダー（16 バイト）をスキップしてコードオブジェクトをロード
with open('chall.pyc', 'rb') as f:
    f.read(16)
    top_co = marshal.load(f)

# 2) 定数やネストしたコードオブジェクトを再帰的に探索
def walk_code(co):
    print('---', co.co_name or '<module>', '---')
    # 定数のうち、bytes/list で flag_enc が含まれるはず
    for c in co.co_consts:
        if isinstance(c, (bytes, list)):
            print('CONST:', c)
    # 名前解決（flag, range, input, print などが出てくる）
    print('NAMES:', co.co_names)
    # ネストした関数／コンストラクタ
    for c in co.co_consts:
        if isinstance(c, types.CodeType):
            walk_code(c)

walk_code(top_co)

# 3) 最後に dis をかければ、ループ／XOR／ord()/chr() のロジックが見える
dis.dis(top_co)


(files) pond@laptop-8UQA2MI:~/ctf/cpctf2025/binary/guessing/files$ python hoge.py 
--- <module> ---
NAMES: ('flag_enc', 'flag', 'range', 'len', 'i', 'chr', 'ord', 'input', 'inp', 'print')
  0           RESUME                   0

  1           LOAD_CONST               0 ('CQAWB~v^kVi?bRl? bfLdLb_(wEk/ox/rLcMG@[')
              STORE_NAME               0 (flag_enc)

  3           LOAD_CONST               1 ('')
              STORE_NAME               1 (flag)

  5           LOAD_NAME                2 (range)
              PUSH_NULL
              LOAD_CONST               2 (0)
              LOAD_NAME                3 (len)
              PUSH_NULL
              LOAD_NAME                0 (flag_enc)
              CALL                     1
              CALL                     2
              GET_ITER
      L1:     FOR_ITER                26 (to L2)
              STORE_NAME               4 (i)

  6           LOAD_NAME                1 (flag)
              LOAD_NAME                5 (chr)
              PUSH_NULL
              LOAD_NAME                6 (ord)
              PUSH_NULL
              LOAD_NAME                0 (flag_enc)
              LOAD_NAME                4 (i)
              BINARY_SUBSCR
              CALL                     1
              LOAD_NAME                4 (i)
              BINARY_OP               12 (^)
              CALL                     1
              BINARY_OP               13 (+=)
              STORE_NAME               1 (flag)
              JUMP_BACKWARD           28 (to L1)

  5   L2:     END_FOR
              POP_TOP

  8           LOAD_NAME                7 (input)
              PUSH_NULL
              LOAD_CONST               3 ('Enter flag: ')
              CALL                     1
              STORE_NAME               8 (inp)

  9           LOAD_NAME                8 (inp)
              LOAD_NAME                1 (flag)
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        9 (to L3)

 10           LOAD_NAME                9 (print)
              PUSH_NULL
              LOAD_CONST               4 ('Wrong!')
              CALL                     1
              POP_TOP
              RETURN_CONST             8 (None)

 12   L3:     LOAD_NAME                9 (print)
              PUSH_NULL
              LOAD_CONST               5 ('Correct!')
              CALL                     1
              POP_TOP

 13           LOAD_NAME                9 (print)
              PUSH_NULL
              LOAD_CONST               6 ('Flag: ')
              LOAD_CONST               1 ('')
              LOAD_CONST               7 (('end',))
              CALL_KW                  2
              POP_TOP
              RETURN_CONST             8 (None)


(files) pond@laptop-8UQA2MI:~/ctf/cpctf2025/binary/guessing/files$ python solve.py 
CPCTF{pYc_c4n_b00st_pYtH0n_p3rf0RmAnce}(files) pond@laptop-8UQA2MI:~/ctf/cpctf2025/binary/guessing/files$ 
(files) pond@laptop-8UQA2MI:~/ctf/cpctf2025/binary/guessing/files$ vim solve.py
(files) pond@laptop-8UQA2MI:~/ctf/cpctf2025/binary/guessing/files$ python solve.py 
CPCTF{pYc_c4n_b00st_pYtH0n_p3rf0RmAnce}
(files) pond@laptop-8UQA2MI:~/ctf/cpctf2025/binary/guessing$ cat files/solve.py 
enc = 'CQAWB~v^kVi?bRl? bfLdLb_(wEk/ox/rLcMG@['

for i, b in enumerate(enc):
    print(chr(ord(b)^i), end='')

print()
```
