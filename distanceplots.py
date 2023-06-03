import matplotlib.pyplot as plt
import numpy as np
import math
distances=[10,15,20,25,30,35,40,45,50,55,60,65, 70]
data1 = [10.5,15.4,19.7,24.6,29.5,33.8,38.2,42.6, 46.6, 53.6, 56.7, 59.7, 65.5]
data2 = [50,50,50,50,50, 44.5, 39, 35, 31.5, 28, 24.5,21.5, 19]
for i in range(len(data2)):
    data2[i]*=0.033
err1 = [0.2,0.2,0.2,0.4,0.4,0.4, 1, 1, 1, 1, 1, 1, 1]
err2 = [0.01,0.01,0.01,0.01,0.01,0.02,0.02,0.02,0.02,0.05,0.05,0.05,0.05]
#plt.errorbar(distances, data1, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
#plt.axhline(0)
#plt.xlim(left=0)
#plt.xlabel("Physical Distance from the Sensor (cm)")
#plt.ylabel("Reported Distance from the Sensor (cm) ")
#plt.title("Reported Distance vs. Physical Distance")
#plt.show()

x = np.linspace(0, 75, 100)

def func(x):
    return np.where((x < 30) & (x >= 0), 1.65, 0.033*50 * np.exp(-(x - 30) / 40))



# Create the figure and the first y-axis
fig, ax1 = plt.subplots()
ax1.errorbar(distances, data1, yerr=err1, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
ax1.axline((0,0), slope=1, c=(0,0,1,0.5))
ax1.set_xlabel('Physical Distance from the Sensor (cm)')
ax1.set_ylabel('Reported Distance from the Sensor (cm)', color='r')
ax1.set_ylim((0,70))

# Create the second y-axis
ax2 = ax1.twinx()
ax2.errorbar(distances, data2, yerr=err2, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)
ax2.plot(x,func(x),c=(0,0,1,0.5))
ax2.set_ylabel('Voltage from the PWM Output (V)', color='g')
ax2.set_ylim((0,2))


# Customize the appearance
ax1.tick_params(axis='y', colors='r')
ax2.tick_params(axis='y', colors='g')

plt.title("Voltage Output and Reported Distance vs. Physical Distance")

# Show the plot
plt.show()
