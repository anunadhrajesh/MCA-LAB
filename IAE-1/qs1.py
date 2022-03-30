import matplotlib.pyplot as plt
import numpy as np


plt.xlabel("total")
plt.ylabel("marks")
plt.title("student's score")

total = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
maths = np.array([38, 62, 18, 75, 38, 59, 66, 92, 52, 75, 48])
plt.scatter(total, maths, color="red", marker="*")

total = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
english = np.array([74, 44, 85, 19, 88, 69, 50, 33, 29, 32, 56])
plt.scatter(total, english, color="green", marker="s")


plt.show()
