import tkinter as tk

# 計算機能のための変数とイベント用の関数定義
# Frame のサブクラスを使った実装例

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

#
# tk.Frame を継承したMyFrame というクラスを作り
# その中でウィジェットやコールバック関数（メソッド）を
# 設定する。tkinter をつかう定番
#
class MyFrame(tk.Frame):
#
#      __init__ はクラスオブジェクトを作る際の初期化メソッド
#アンダースコアは前後それぞれ２つずつ
    def __init__(self, master = None):
        super().__init__(master)
# あとで参照しないウィジェットの作成、ローカル変数
        b1 = tk.Button(self,text='1', command=lambda:self.key(1), font=('Helvetica', 14), width=2, bg='#ffffff')
        b2 = tk.Button(self,text='2', command=lambda:self.key(2), font=('Helvetica', 14), width=2, bg='#ffffff')
        b3 = tk.Button(self,text='3', command=lambda:self.key(3), font=('Helvetica', 14), width=2, bg='#ffffff')
        b4 = tk.Button(self,text='4', command=lambda:self.key(4), font=('Helvetica', 14), width=2, bg='#ffffff')
        b5 = tk.Button(self,text='5', command=lambda:self.key(5), font=('Helvetica', 14), width=2, bg='#ffffff')
        b6 = tk.Button(self,text='6', command=lambda:self.key(6), font=('Helvetica', 14), width=2, bg='#ffffff')
        b7 = tk.Button(self,text='7', command=lambda:self.key(7), font=('Helvetica', 14), width=2, bg='#ffffff')
        b8 = tk.Button(self,text='8', command=lambda:self.key(8), font=('Helvetica', 14), width=2, bg='#ffffff')
        b9 = tk.Button(self,text='9', command=lambda:self.key(9), font=('Helvetica', 14), width=2, bg='#ffffff')
        b0 = tk.Button(self,text='0', command=lambda:self.key(0), font=('Helvetica', 14), width=2, bg='#ffffff')
        bc = tk.Button(self,text='C', command=self.clear, font=('Helvetica', 14), width=2, bg='#ff0000')
        bp = tk.Button(self,text='+', command=self.plus, font=('Helvetica', 14), width=2, bg='#00ff00')
        bmi = tk.Button(self,text='-', command=self.minus, font=('Helvetica', 14), width=2, bg='#00ff00')
        bmu = tk.Button(self,text='x', command=self.multiple, font=('Helvetica', 14), width=2, bg='#00ff00')
        bd = tk.Button(self,text='÷', command=self.devide, font=('Helvetica', 14), width=2, bg='#00ff00')
        be = tk.Button(self,text='=', command=self.eq, font=('Helvetica', 14), width=2, bg='#00ff00')

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

    # 他のメソッドで参照する数値を表示するウィジェット、クラスオブジェクトの
    #変数として作成、頭にself. がつく
        self.e = tk.Entry(self)
        self.e.grid(row=0,column=0,columnspan=4)
    # クラスの定義では
    # メソッドの最初の引数はself, 中でクラスオブジェクトの変数、
    # メソッドはself をつけて参照
    #
    def key(self,n):
        global current_number
        current_number = current_number * 10 + n
        self.show_number(current_number)

    def clear(self):
        global current_number
        current_number = 0
        self.show_number(current_number)

    def plus(self):
        do_plus()
        self.show_number(first_term)

    def minus(self):
        do_minus()
        self.show_number(first_term)

    def multiple(self):
        do_multiple()
        self.show_number(first_term)

    def devide(self):
        do_devide()
        self.show_number(first_term)

    def eq(self):
        do_eq()
        self.show_number(result)

    def show_number(self, num):
        self.e.delete(0,tk.END)
        self.e.insert(0,str(num))

#
# ここからメインプログラム
#
root = tk.Tk()
f = MyFrame(root)
f.pack()
f.mainloop()
