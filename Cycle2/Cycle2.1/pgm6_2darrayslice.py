import numpy as np

x = np.array([[2, 4, 6,1], [6, 8, 10,1],[1, 2, 1,1], [1, 1, 1,1]])
print(x)
#1
print("excluding first row\n",x[1:])
#2
print("excluding last column\n",x[:,:3])
#3
print("Display the elements of 1st and 2nd column in 2nd and 3rd row")
print(x[1:3,0:2])
#4
print("dispaly 2 and 3 element",x[:1,1:3])
#5
print("display 2nd and 3rd element of 1st row")
print(x[0:1,1:3])
#6
arr=np.array([1,6,8,10,1,1,2])
sarr=np.sort(arr)[::-1]
print(sarr)

