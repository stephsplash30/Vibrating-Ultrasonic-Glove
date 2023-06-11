import matplotlib.pyplot as plt
import numpy as np
import math
distances=[10, 15,20,25,30,35,40,45,50,55,60,65,70]
data = 0.033 * [50,50,50,50,50, 44.5, 39, 35, 31.5, 28, 24.5,21.5, 19]

x = np.linspace(0, 75, 100)

def func(x):
    return np.where((x < 30) & (x >= 0), 50, 50 * np.exp(-(x - 30) / 40))


plt.plot(x,func(x),c=(0,0,1,0.5))

err = [0,0,0,0,0,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25]
plt.errorbar(distances, data, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.xlim((0,75))
plt.ylim((0,75))
plt.xlabel("Physical Distance from the Sensor (cm)")
plt.ylabel("PWM Percentage (%) ")
plt.title("PWM Percentage vs. Physical Distance")
plt.show()
