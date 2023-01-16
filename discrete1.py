from itertools import product
A=[1,2,3,4]
print("A = " + str(A))
R1 = [(i,j) for i,j in product(A,repeat=2) if i%j == 0 ]
R2 = [(i,j) for i,j in product(A,repeat=2) if i<=j]
print("R1 = " + str(R1))
print("R2 = " + str(R2))