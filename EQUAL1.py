import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([3,4,5,6,7])
print("First array:",arr1)
print("Second array:",arr2)
if np.array_equal(arr1,arr2):
	print("Arrays are equal")
else:
	print("Arrays are not equal")
