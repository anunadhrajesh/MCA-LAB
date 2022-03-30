import matplotlib.pyplot as plt
import numpy as np

plt.title("Student Transport Data")
plt.xlabel("mode of transport")
plt.ylabel("frequency")

x = np.array(["Walking", "Cycling", "Car", "Bus", "Train"])
y = np.array([29, 15, 35, 18, 3])
plt.bar(x,y, color ="g", width = 0.1)


plt.show()