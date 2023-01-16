def func(x):
    return x*x - 4*x - 10
def bisection(a,b):
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return -1
    c = a
    while ((b-a) >= 0.01):
        c = (a+b)/2
        if (func(c) == 0.0):
            break
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c
    print("The value of root is : ","%.4f"%c)
a =-2
b = -1.5
bisection(a, b)