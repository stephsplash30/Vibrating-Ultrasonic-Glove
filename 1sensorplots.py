import matplotlib.pyplot as plt
plt.figure(1)
distances = [20, 20, 40, 40, 57, 57, 77, 77]
top=[4,-5,5,-8,8,-10,15,-13]
mid=[3,-5,5,-8,7.5,-10,12,-15]
bot=[3,-4,4,-7,7,-9,10,-14]
err = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
plt.errorbar(distances, top, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.errorbar(distances, mid, yerr=err, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)
plt.errorbar(distances, bot, yerr=err, fmt="o",c=(0,0,1,0.5),ms=4,capsize=2)
plt.axhline(0)
plt.xlim(left=0)
plt.xlabel("Distance from the Sensor")
plt.ylabel("Maximum Range Up(+)/Down(-)")
plt.show()

plt.figure(2)
top=[-3,4,-4,6,-4.5,9,-8,10]
mid=[-2.5,3.5,-3,6,-4,8,-7,11]
bot=[-2.5,3,-3.5,5.5,-5,7,-6,10]
plt.errorbar(distances, top, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.errorbar(distances, mid, yerr=err, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)
plt.errorbar(distances, bot, yerr=err, fmt="o",c=(0,0,1,0.5),ms=4,capsize=2)
plt.axhline(0)
plt.xlim(left=0)
plt.xlabel("Distance from the Sensor")
plt.ylabel("Maximum Range Left(+)/Right(-)")
plt.show()
import matplotlib.pyplot as plt

plt.figure(3)
distances = [77, 57, 40, 20]
top=[105,98,95,38]
mid=[100,95,93,35]
bot=[95,93,91,34]
err = [0.5,0.5,0.5,0.5]
plt.errorbar(distances, top, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2, label = "top sensor")
plt.errorbar(distances, mid, yerr=err, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2, label = "middle sensor")
plt.errorbar(distances, bot, yerr=err, fmt="o",c=(0,0,1,0.5),ms=4,capsize=2, label = "bottom sensor")
plt.xlim(left=0)
plt.xlabel("Distance from the Sensor")
plt.ylabel("Max Height")
plt.legend()
plt.show()


plt.figure(4)
top=[90,90,90,34]
mid=[88,88,88,32]
bot=[86,86,86, 30]
plt.errorbar(distances, top, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2,label = "top sensor")
plt.errorbar(distances, mid, yerr=err, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2,label = "middle sensor")
plt.errorbar(distances, bot, yerr=err, fmt="o",c=(0,0,1,0.5),ms=4,capsize=2,label = "bottom sensor")
plt.xlim(left=0)
plt.xlabel("Distance from the Sensor")
plt.ylabel("Height of sensor")
plt.legend()
plt.show()

plt.figure(5)
top=[77,80,82,29]
mid=[73,78,80,27]
bot=[72,77,79,26]
plt.errorbar(distances, top, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.errorbar(distances, mid, yerr=err, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)
plt.errorbar(distances, bot, yerr=err, fmt="o",c=(0,0,1,0.5),ms=4,capsize=2)
plt.xlim(left=0)
plt.xlabel("Distance from the Sensor")
plt.ylabel("Minimum Height")
plt.show()

plt.figure(6)
distances1 = [77,57,40,20,20,40,57,77]
top=[-8,-4.5,-4,-3,4,6,9,10]
mid=[-7,-4,-3,-2.5,3.5,6,8,11]
bot=[-6,-5,-3.5,-2.5,3.5,5.5,6,10]
err1 = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
plt.axhline(0)
plt.errorbar(distances1, top, yerr=err1, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.errorbar(distances1, mid, yerr=err1, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)
plt.errorbar(distances1, bot, yerr=err1, fmt="o",c=(0,0,1,0.5),ms=4,capsize=2)
plt.xlim(left=0)
plt.xlabel("Distance from the Sensor")
plt.ylabel("Minimum Height")
plt.show()
