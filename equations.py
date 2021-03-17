
def exponent(x:float)->float:
    exp=1
    for i in range(1,100):
        j=1
        up=x
        down=float(i)
        while j<i:
            up=up*x
            down=down*(i-j)
            j+=1
        exp+=up/down
    return exp

def Ln(x:float)->float:
    if x<=0:
        return 0.0
    yn=0.0
    for i in range(1,100):
        yn+=2*((x-exponent(yn))/(x+exponent(yn)))
    return yn

def XtimesY(x:float,y:float)->float:
    if x==0:
        result = 0.0
    elif x>0:
        result = exponent(y*Ln(x))
    else:
        if y % 1 != 0:
            return 0.0
        if y % 2 == 0:
            result = exponent((y)*Ln((-1)*(x)))
        else:
            result = exponent((y)*Ln((-1)*(x)))*-1
        
    # return float('%0.6f' % result)
    return result

def sqrt(x:float,y:float)->float:
    return XtimesY(y, 1/x)

def calculate(x:float)->float:
    result = exponent(x)*XtimesY(7, x)*XtimesY(x, -1)*sqrt(x, x)
    if result == -0.0:
        result = 0.0
    return float('%0.6f' % result)

x=float(input())
print(calculate(x))
