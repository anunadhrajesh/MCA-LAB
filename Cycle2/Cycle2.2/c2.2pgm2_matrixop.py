import numpy as np


arr1=np.arange(4,8).reshape(2,2)
print("\narray\n",arr1)
#1
print("\ncube using power\n")
b=np.power(arr1,3)
print(b)
f=arr1**3
print("\n",f)
print("\ncube using multiply\n")
c=np.multiply(arr1,arr1)
d=np.multiply(c,arr1)
print("\n",d)

e=arr1*arr1*arr1
print("\n",e)

#2
print("\nidentity matrix\n")
h=np.identity(2)
print("\n",h)
#3
print("\nDisplay each element of the matrix to different powers.")
i=np.power(arr1[0][0],2)
j=np.power(arr1[0][1],3)
k=np.power(arr1[1][0],4)
m=np.power(arr1[1][1],5)
print("\n",i)
print("\n",j)
print("\n",k)
print("\n",m)
#4
print("\nCreate a matrix Y with same dimension as X and perform the operation X 2 +2Y")
arr2=np.arange(0,4).reshape((2,2))
print("\n",arr2)
n=np.power(arr1,2)
o=np.multiply(2,arr2)
print("\n",o)
p=np.add(n,o)
print("\n",p)