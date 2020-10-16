import tkinter as tk

# 計算機能のための変数とイベント用の関数定義

# 二項演算のモデル
# 入力中の数字
current_number = 0
# 第一項
first_term = 0
# 第二項
second_term = 0
# 演算子
operator = '+'
# 結果
result = 0

def do_plus():
    "+ キーが押されたときの計算動作、第一項の設定と入力の数字のクリア"
    global current_number
    global first_term
    global operator

    first_term = current_number
    operator = '+'
    current_number  = 0

def do_minus():
    global current_number
    global first_term
    global operator

    first_term = current_number
    operator = '-'
    current_number  = 0

def do_multiple():
    global current_number
    global first_term
    global operator

    first_term = current_number
    operator = '*'
    current_number  = 0

def do_devide():
    global current_number
    global first_term
    global operator

    first_term = current_number
    operator = '÷'
    current_number  = 0

def do_eq():
    "= キーが押されたときの計算動作, 第二項の設定、加算の実施、入力中の数字のクリア"
    global second_term
    global result
    global current_number
    global operator

    second_term = current_number

    if(operator == '+'):
        result = first_term + second_term
    elif(operator == '-'):
        result = first_term - second_term
    elif(operator == '*'):
        result = first_term * second_term
    else:
        result = first_term // second_term
    current_number = 0


# 数字キーを一括処理する関数
def key(n):
    global current_number
    current_number = current_number * 10 + n
    show_number(current_number)

def clear():
    global current_number
    current_number = 0
    show_number(current_number)

def plus():
    do_plus()
    show_number(first_term)

def minus():
    do_minus()
    show_number(first_term)

def multiple():
    do_multiple()
    show_number(first_term)

def devide():
    do_devide()
    show_number(first_term)

def eq():
    do_eq()
    show_number(result)

def show_number(num):
    e.delete(0,tk.END)
    e.insert(0,str(num))

#tkinterでの画面の構成
root = tk.Tk()      #Tk()でウィンドウ生成
f = tk.Frame(root, bg='#ffffc0')      #Frameコンテナ生成
f.grid()        #Frameを貼り付け

# ウィジェットの作成

b1 = tk.Button(f,text='1', command=lambda:key(1), font=('Helvetica', 14), width=2, bg='#ffffff')
b2 = tk.Button(f,text='2', command=lambda:key(2), font=('Helvetica', 14), width=2, bg='#ffffff')
b3 = tk.Button(f,text='3', command=lambda:key(3), font=('Helvetica', 14), width=2, bg='#ffffff')
b4 = tk.Button(f,text='4', command=lambda:key(4), font=('Helvetica', 14), width=2, bg='#ffffff')
b5 = tk.Button(f,text='5', command=lambda:key(5), font=('Helvetica', 14), width=2, bg='#ffffff')
b6 = tk.Button(f,text='6', command=lambda:key(6), font=('Helvetica', 14), width=2, bg='#ffffff')
b7 = tk.Button(f,text='7', command=lambda:key(7), font=('Helvetica', 14), width=2, bg='#ffffff')
b8 = tk.Button(f,text='8', command=lambda:key(8), font=('Helvetica', 14), width=2, bg='#ffffff')
b9 = tk.Button(f,text='9', command=lambda:key(9), font=('Helvetica', 14), width=2, bg='#ffffff')
b0 = tk.Button(f,text='0', command=lambda:key(0), font=('Helvetica', 14), width=2, bg='#ffffff')
bc = tk.Button(f,text='C', command=clear, font=('Helvetica', 14), width=2, bg='#ff0000')
bp = tk.Button(f,text='+', command=plus, font=('Helvetica', 14), width=2, bg='#00ff00')
bmi = tk.Button(f,text='-', command=minus, font=('Helvetica', 14), width=2, bg='#00ff00')
bmu = tk.Button(f,text='x', command=multiple, font=('Helvetica', 14), width=2, bg='#00ff00')
bd = tk.Button(f,text='÷', command=devide, font=('Helvetica', 14), width=2, bg='#00ff00')
be = tk.Button(f,text='=', command=eq, font=('Helvetica', 14), width=2, bg='#00ff00')

# Grid 型ジオメトリマネージャによるウィジェットの割り付け

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
bc.grid(row=1,column=3)
be.grid(row=4,column=3)
bp.grid(row=2,column=3)
bmi.grid(row=3,column=3)
bmu.grid(row=4,column=1)
bd.grid(row=4,column=2)

# 数値を表示するウィジェット
e = tk.Entry(f)
e.grid(row=0,column=0,columnspan=4)
clear()

#ここからGUIがスタート
root.mainloop()
