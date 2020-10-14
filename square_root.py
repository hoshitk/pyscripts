#
def square_root(x):
    '引数ｘの平方根を求める'
    rnew = x
    #
    diff = rnew - x/rnew
    if(diff<0):
        diff = -diff
    while(diff > 1.0E-6):
        r1=rnew
        r2=x/r1
        rnew=(r1+r2)/2
        print(r1,rnew,r2)
        diff= r1 - r2
        if(diff<0):
            diff = -diff
    return rnew
# ここからメイン
v = 2
r = square_root(v)
print("結果は ",r)
