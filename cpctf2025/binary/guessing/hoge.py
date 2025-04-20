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

