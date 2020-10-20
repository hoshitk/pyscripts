import numpy as np
import pandas as pd
import os
#
# データあるフォルダに移動、文字列にr を付けて特殊な文字の解釈を止める
#
# pandas は日本語のファイル名をうまく処理できない
#
os.chdir(r"/home/hoshitk/works/pyscripts")
df = pd.read_csv("sample2.csv")
#
# 水平方向(axis = 1) に総和をとり、Total という列を作る
df['Total'] = df.sum(axis=1)
# データフレームdf を表示
print(df)
# データフレームdf の要約統計量を表示
print(df.describe())
