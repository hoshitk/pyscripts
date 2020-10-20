#
#matplotlib でヒストグラムを描く
#
import matplotlib
#
# 出力先としてtkinter を設定、pyplot のインポートより前に
#
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
#
# matplotlib で日本語表示を可能にする
matplotlib.rc('font', **{'family':'IPAPGothic'})
#
# ヒストグラムの作成
#
data = np.random.randn(1000)
plt.hist(data,bins=20)
#
# タイトル、軸ラベルを設定
#
plt.title('ヒストグラム')
plt.xlabel('データの値')
plt.ylabel('頻度')
#
# 表示
#
plt.show()
