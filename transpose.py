import numpy as np
a=int(input("Enter the number of rows:"))
b=int(input("Enter the number of columns:"))
matrix=[]
print("Enter the elements:")
for i in range(a):
	a=[]
	for j in range(b):
   		a.append(int(input()))
	matrix.append(a)
print(matrix)
result=np.transpose(matrix)
print(result)
