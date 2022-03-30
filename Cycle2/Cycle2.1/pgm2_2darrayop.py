import numpy as np
array = np.arange(6).astype(complex).reshape(2,3)
print(array)
print("rows and columns\n", array.shape)
print("dimention\n", array.ndim)
arr2 = array.reshape(3,2)
print("reshape\n", arr2)