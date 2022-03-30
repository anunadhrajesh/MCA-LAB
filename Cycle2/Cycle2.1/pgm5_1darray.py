import numpy as np

array=np.arange(0,15,2)
print(array)
print("Elements from index 2 to 8\n",array[2:8])
print("Last 3 elements of the array using negative index\n",array[-3:])
print("Alternate elements of the array",array[::2])