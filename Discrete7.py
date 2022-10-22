# Python3 Program to interpolate using
# newton forward interpolation
 
# calculating u mentioned in the formula
def u_cal(u, n):
 
    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp
 
# calculating factorial of given number n
def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
 
# Driver Code
 
# Number of values given
n = 8
x = [1,2,3,4,5,6,7,8]
     
# y[][] is used for difference table
# with y[][0] used for input
y = [[0 for i in range(n)]
        for j in range(n)]
y[0][0] = 1
y[1][0] = 8
y[2][0] = 27
y[3][0] = 64
y[4][0] = 125
y[5][0] = 216
y[6][0] = 343
y[7][0] = 512
 
# Calculating the forward difference
# table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]
 
# Displaying the forward difference table
for i in range(n):
    print(x[i], end = "\t")
    for j in range(n - i):
        print(y[i][j], end = "\t")
    print("")
 
# Value to interpolate at
value = 7.5
 
# initializing u and sum
sum = y[0][0]
u = (value - x[0]) / (x[1] - x[0])
for i in range(1,n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i)
 
print("\nValue at", value,
      "is", round(sum, 6))
 
# This code is contributed by mits