# 今のワーキングディレクトリ（作業中のフォルダ）
# を調べるために OSモジュールを importします

import os

# 今のワーキングディレクトリを得て画面に表示します
print(os.getcwd())

# 日本語ファイル.txt という名称のファイルを作成し、内容を書き出します

f = open('日本語ファイル.txt','w')
f.write('日本語\n日本語\n日本語\n ')
f.close()

# 日本語ファイル.txt を読み込み用にopen して、その内容を表示します

f = open('日本語ファイル.txt','r')
s = f.read()
f.close()
print(s)

# with open(ファイル名などopen 関数の引数, 'a(append)') as ファイルオブジェクト用変数:
#           ファイルを操作するブロック
with open('日本語ファイル.txt','a') as f:
    f.write('追記append\n')

# 日本語ファイル.txt を読み込み用にopen して、その内容を表示します

f = open('日本語ファイル.txt','r')
s = f.read()
f.close()
print(s)
