from itertools import product
s=[1,2,3,4]
print("s = " + str(s))

R1 = [(i,j) for i,j in product(s,repeat=2) if i%j == 0 or j%i==0]
R2 = [(i,j) for i,j in product(s,repeat=2) if i<=j]

print("R1 = " + str(R1))
print('R2 = ' + str(R2))