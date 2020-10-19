class Dentaku():
    def __init__(self):
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self_operation = "+"

    def do_operation(self):
        if self.operation == "+":
            self.result = self.first_term + self.second_term
        elif seif.operation == "-":
            self.result = self.first_term - self.second_term

# ここからメインプログラム
dentaku = Dentaku()
dentaku2 = Dentaku()
while True:
    f = int(input("First term "))
    dentaku.first_term = f
    o = input("Operation ")
    dentaku.operation = o
    s = int(input("Second term "))
    dentaku.second_term = s
    dentaku.do_operation()
    r = dentaku.result

    f2 = r
    dentaku2.first_term = f2
    o2 = input("Operation ")
    dentaku2.operation = o2
    s2 = int(input("Second term "))
    dentaku2.second_term = s2
    dentaku2.do_operation()
    r2 = dentaku2.result

    print("Result ", r, "Result2 ",r2)
