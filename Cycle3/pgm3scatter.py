import matplotlib.pyplot as plt
import numpy as np


plt.xlabel("Month of year", fontsize = 18)
plt.ylabel("Sales of Segments", fontsize = 18)
plt.title("Sales Data")


x = np.array(["jan", "feb", "mar", "apr", "may", "jun", "july", "aug", "sep", "oct", "nov", "dec"])
afseg = np.array([173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131])
plt.scatter(x, afseg, color = "hotpink")


x = np.array(["jan", "feb", "mar", "apr", "may", "jun", "july", "aug", "sep", "oct", "nov", "dec"])
lseg = np.array([189, 189, 105, 112, 173, 109, 151, 197, 174, 145, 177, 161])
plt.scatter(x, lseg, color = "y")

x = np.array(["jan", "feb", "mar", "apr", "may", "jun", "july", "aug", "sep", "oct", "nov", "dec"])
slseg = np.array([185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110])
plt.scatter(x, slseg, color = "b")

plt.show()