#
#matplotlib 基本の使い方
#
import matplotlib
#
# 出力先としてtkinter をuse で設定、pyplot のインポートより前に
#
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
#
# matplotlib で日本語表示を可能にする
#
#
#matplotlib.rc('font', **{'family':'Yu Gothic'}) #ダメ
#
# 教育用端末なら下の設定で
matplotlib.rc('font', **{'family':'IPAPGothic'})
#
# 3 本の線グラフを書く
#
plt.plot([1,2,3],'k-',label='系列1')  #黒の実線
plt.plot([2,3,4],'r--',label='系列2') #赤の破線
plt.plot([3,4,5],'b--o',label='系列3')    #青の破線、〇のマーカ
#
plt.title('タイトル')
plt.xlabel('横軸')
plt.ylabel('縦軸')
plt.legend() # 凡例
plt.show()
