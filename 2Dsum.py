import numpy as np 
arr=np.array([[3,5,7,8],[1,2,4,6]])
print(arr)
sum_all=np.sum(arr)
sum_row=np.sum(arr,axis=1)
sum_column=np.sum(arr,axis=0)
print("Sum of all elements:",sum_all)
print("Sum of each row:",sum_row)
print("Sum of each column:",sum_column)
