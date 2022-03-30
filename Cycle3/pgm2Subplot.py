import matplotlib.pyplot as plt
import numpy as np

#plot 1
x = np.array(['mon', 'tues', 'wed', 'thu', 'fri'])
y = np.array([300, 450, 150, 400, 650])



plt.subplot(2, 1, 1)
plt.title("Sales Data 1", loc = "right")
plt.xlabel("Days of week")
plt.ylabel("Sale of Drinks")
plt.plot(x,y, color = 'cyan', linestyle = 'dotted', marker = 'H', mec = 'black', mfc = 'm')
plt.grid(color = 'blue', linestyle = 'dotted')

#plot 2
x = np.array(['mon', 'tues', 'wed', 'thu', 'fri'])
y = np.array([400, 500, 350, 300, 500])

plt.subplot(2, 1, 2)
plt.title("Sales Data 2")
plt.xlabel("Days of week")
plt.ylabel("Sale of Food")
plt.plot(x,y, color = 'y', linestyle = '--', marker = 'D', mec = 'r', mfc = 'g')
plt.grid(color = 'blue', linestyle = 'dotted')

plt.subplots_adjust(top=2.5,
                    bottom=1.5,
                    wspace=0.4, 
                    hspace=0.4)
plt.show()