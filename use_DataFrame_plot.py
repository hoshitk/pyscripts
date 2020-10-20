import numpy as np
import pandas as pd
import os
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
#
#データあるフォルダに移動、文字列にr を付けて特殊な文字の解釈を止める
#
#pandas は日本語のファイル名をうまく処理できない
#個人環境に合わせたディレクトリ（フォルダ）の移動
os.chdir(r"/home/hoshitk/works/pyscripts")
#
#教育用端末なら以下で
#os.chdir(r"M:¥Documents")
#
df = pd.read_csv("sample2.csv")
#
#
# 折れ線グラフ
#

df.plot()
print("次に進むにはグラフウィンドウを閉じてください")
plt.show()
#
# 積み上げ棒グラフ
#
df.plot.bar(stacked=True)
print("次に進むにはグラフウィンドウを閉じてください")
plt.show()
#
# 散布図
#
df.plot.scatter('Japanese','English')
print("次に進むにはグラフウィンドウを閉じてください")
plt.show()
#
# 水平方向(axis = 1) に総和をとり、Total という列を作る
#
df['Total'] = df.sum(axis=1)

#
# ヒストグラム
#
df['Total'].plot.hist()
print("次に進むにはグラフウィンドウを閉じてください")
plt.show()
