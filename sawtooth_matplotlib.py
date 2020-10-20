#
#
# 鋸歯状波をplot する
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
import math
matplotlib.rc('font', **{'family':'IPAPGothic'})
#
#正弦波の重ね合わせで鋸波を近似する
#
# w = sin(t) + sin(2t)/2 + sin(3t)/3 + sin(4t)/4 ...
#
#
cycles = 2
steps = 1000
harmonics = 8
maxx = 2
#
# numpyのarrayで配列用意
#
x = np.zeros(steps)
datalist = np.zeros((steps, harmonics+1))
# 計算してarrayに格納
for i in range(steps):
    angle_in_degree = 360*cycles*i/steps
    angle = np.radians(angle_in_degree)
    # x軸の値を入れてく
    x[i] = angle_in_degree
    w = 0
    for j in range(1, harmonics+1):
        w += np.sin(angle*(j))/j
        datalist[i,j-1] = w
#
# 凡例用のリスト
#
legend_label=[]
#
#
#
for j in range(1,harmonics+1):
    legend_label.append(str(j)+'項までの和')
#
# プロット
#
datalist.shape
plt.plot(x, datalist)
plt.title('鋸歯状波のフーリエ近似')
plt.xlabel('角度')
plt.ylabel('振幅')
plt.legend(legend_label)
plt.show()
