import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
# messagebox, filedialog は明示的なインポートが必要
#
# tk.Frame を継承したMyFrame というクラスを作り
# その中でウィジェットやコールバック関数（メソッド）を設定する。
# tkinter をつかう定番
#
class MyFrame(tk.Frame):
#      __init__はクラスオブジェクトを作る際の初期化メソッド
    def __init__(self, master = None):
        super().__init__(master)
        self.master.title('Simple Editor')

# メニューを作るmenubar -> filemenu -> Open, Save as, Exit
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Open", command = self.openfile)
        filemenu.add_command(label = "Save as...", command = self.saveas)
        filemenu.add_command(label = "Exit", command = self.master.destroy)
        filemenu.add_cascade(label = "File", menu = filemenu)
        self.master.config(menu = menubar)

# 編集用Text ウィジェットをクラスの変数editbox としてつくる
        self.editbox = tk.Text(self)
        self.editbox.pack()

# ファイルを開くメソッド、関数とちがいself という引数が必要
    def openfile(self):
# filedialog でファイル名を得る
        filename = tkinter.filedialog.askopenfilename()
# filename が空でなければ処理
        if filename:
            tkinter.messagebox.showinfo("Filename","Open: "+filename)
# with 文でfile という変数でファイルを開く
            with open(filename,'r') as file:
                text = file.read()
# Text ウィジェットeditbox にファイル内容を設定
            self.editbox.delete('1.0',tk.END)
            self.editbox.insert('1.0',text)
        else:
            tkinter.messagebox.showinfo("Filename","Canceled")

# ファイルに保存するメソッド
    def saveas(self):
#    with 文でfile という変数でファイルを開く
        filename = tkinter.filedialog.asksaveasfilename()
        if filename:
            with open(filename,'w') as file:
                text = file.write(self.editbox.get('1.0',tk.END))
            tkinter.messagebox.showinfo("Filename","Saved AS:"+filename)
        else:
            tkinter.messagebox.showinfo("Filename","Canceled")

# ここからメインプログラム
root = tk.Tk()
f = MyFrame(root)
f.pack()
f.mainloop()
