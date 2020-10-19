import tkinter as tk
import tkinter.filedialog
import math
#
# tkinter のfiledialog だけを利用する例
#
# root ウィンドウはwithdrow() メソッドを読んで隠す
root = tk.Tk()
root.withdraw()
#
# 書き出し用のfiledialog を読んでファイル名を得る
#
filename = tkinter.filedialog.asksaveasfilename()
#
# ファイル名がもらえなければ終了
#
if filename:
    pass
else:
    print("No file specified")
    exit()
#
# 正弦波の重ね合わせで鋸波を近似する
#
# w = sin(t) + sin(2t)/2 + sin(3t)/3 + sin(4t)/4 ...
#
# 2周期分、全体は1000 ステップで、高調波は5番目まで
#
cycles = 2
steps = 1000
harmonics = 5
# ファイルが開けないときのエラー対応
try:
# ファイルを開く
    with open(filename,'w') as file:
        for i in range(steps):
            angle_in_degree = 360*cycles*i/steps
            angle = math.radians(angle_in_degree)
            s = str(angle_in_degree)
            w = 0
            for i in range(1, harmonics+1):
                w += math.sin(angle*(i))/i
                s = s+","+str(w)
        #   print(s)
            file.write(s+"\n")
        print("Writing to file "+ filename + " is finished")
except IOError:
    print("Unable to open file")
