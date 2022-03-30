import numpy as np

a= np.array([[1, 2, 3], 
              [2, 1, 2],
              [3, 2, 1]])
x=np.transpose(a)
print("\transpose",a)
c=np.array_equal(a, x)
print("symmetric or not:" ,c)


b=np.negative(a)
d=np.array_equal(x,b)
print("skew symmetric or not:",d)