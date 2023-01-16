MAX_ITER = 1
def f(x): 
    return (x*x - x - 2)
def false_position(a,b):
    if f(a) * f(b) >= 0:
        print("You not assumed right a and b")
        return
    c = a
    for i in range(MAX_ITER):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if f(c) == 0:
            break
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c
    print('The Value of root:',round(c,4))
a = int(input("Enter the value of a:"))
b = int(input("Enter the Value of b:"))
false_position(a,b)