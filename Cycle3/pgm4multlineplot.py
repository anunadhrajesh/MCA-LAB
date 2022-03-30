import matplotlib.pyplot as plt

x1 = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
x2 = [173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131]
plt.plot(x1, x2, color = 'hotpink', label = 'line 1', ls = '-.')

y1 = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y2 = [189, 189, 105, 112, 173, 109, 151, 197, 174, 145, 177, 161]
plt.plot(y1, y2, color = 'y', label = 'line 2', linestyle = 'dashed')

z1 = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
z2 = [185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110]
plt.plot(z1, z2, color = 'blue', label = 'line 3',linestyle = 'dotted')

plt.xlabel("Month of year", fontsize = 18)
plt.ylabel("Sales of Segments", fontsize = 18)
plt.title("Sales Data")

plt.legend()
plt.show()