#
# subplot を使う例
#
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
#
# テキストで日本語を表示できるようにする
#
matplotlib.rc('font', **{'family':'IPAPGothic'})
#
# 3 つのsubplot を作成、間隔を調整
#
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
plt.subplots_adjust(hspace=0.5, wspace= 0.5)
#
# 1 つめに線グラフを出力
#
data = np.random.randn(100).cumsum()
ax1.plot(data)
ax1.set_title('線グラフ')
ax1.set_xlabel('時間')
ax1.set_ylabel('場所')
#
# 2 つめに散布図を出力
#
datax = np.random.randn(100)
datay = datax + np.random.randn(100)*0.3
ax2.scatter(datax,datay,label='データ1')

datax = np.random.randn(100)
datay = 0.6*datax + np.random.randn(100)*0.4
ax2.scatter(datax,datay,color='red',label='データ2')

ax2.set_title('散布図')
ax2.set_xlabel('属性1')
ax2.set_ylabel('属性2')
ax2.legend()
#
# 3 つめにヒストグラムを出力
#
data = np.random.randn(1000)
ax3.hist(data,bins=20)
ax3.set_title('ヒストグラム')
ax3.set_xlabel('データの値')
ax3.set_ylabel('頻度')
#
# グラフを表示
#
plt.show()
