#
#
# Numpy のデータをplot する例題
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rc('font', **{'family':'IPAPGothic'})
#
# x の1乗~ 4 乗をプロットする
#
steps = 100
order = 4
maxx = 2
#
# 要素の値0 でsteps 行、order 列の行列を作成
#
datalist = np.zeros((steps, order))
#
# 凡例用のリスト
#
legend_label=[]
#
# x の値をlinspace で作成
#
x = np.linspace(0,maxx,steps)
#
# 各列について、一気に計算する
#
for j in range(1,order+1):
    datalist[:,j-1] = x**j
    legend_label.append(str(j)+'乗')
#
# プロット
#
plt.plot(x, datalist)
plt.title('x のべき乗')
plt.xlabel('x')
plt.ylabel('x**n')
plt.legend(legend_label)
plt.show()
