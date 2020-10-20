#
#matplotlib で散布図を描く
#
import matplotlib
#
# 出力先としてtkinter をuse で設定、pyplot のインポートより前に
#
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
#
# matplotlib で日本語表示を可能にする
#
matplotlib.rc('font', **{'family':'IPAPGothic'})
#
# ランダムなデータの作成
#
datax = np.random.randn(100)
datay = datax + np.random.randn(100)*0.3
#
# 散布図の描画
#
plt.scatter(datax,datay,label='データ1')
#
# 別のデータの作成
#
datax = np.random.randn(100)
datay = 0.6*datax + np.random.randn(100)*0.4
#
# 色を指定して散布図を作成
#
plt.scatter(datax,datay,color='red',label='データ2')
#
# タイトル、軸ラベル、凡例の記入
#
plt.title('タイトル')
plt.xlabel('横軸')
plt.ylabel('縦軸')
plt.legend()
#
# 表示
#
plt.show()
