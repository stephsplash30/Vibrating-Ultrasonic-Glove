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