import numpy as np

print("\nLarge matrix")
arr1=np.arange(1,37).reshape((6,6))
print(arr1)
print("\nsmall matrix")
arr2=np.arange(1,10).reshape((3,3))
print(arr2)
print("\ncutout portion")
a=arr1[0:3,1:4]
print(a)
print("\nmultiplying with smaller matrix")
c=np.multiply(a,arr2)
print(c)
print("\nfinal matrix")
arr1[0:3,1:4]=c
print(arr1)