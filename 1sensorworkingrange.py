import matplotlib.pyplot as plt
import numpy as np
distances = [0,20, 40, 57, 77]
high=[0,4,5,8,15]
low=[0,-5,-8,-10,-13]
left=[0,2,4.5,6,7.5]
right=[0,-1,-3,-4,-5]

ph= np.polyfit(distances,high, deg=1)
pl= np.polyfit(distances,low, deg=1)
pll=np.polyfit(distances,left, deg=1)
pr=np.polyfit(distances,right, deg=1)

err = [0, 1,1,1,1]
errr= [0,0.5,0.5,0.5,0.5]
def func(x, p):
    return p[0]*x+p[1]

x = np.linspace(0, 80, 100)
y1=func(x,ph)
y2=func(x,pl)
plt.fill_between(x,y1,y2,color=(0,0,1,0.25), label = "Estimated Working Range")

plt.errorbar(distances, high, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2, label = "Raw Data")
plt.errorbar(distances, low, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.title('Working Range of Single Sensor Up/Down')
plt.xlabel('Distance from the Sensor (cm)')
plt.ylabel('Maximum Range Up(+)/Down(-) (cm)')
plt.legend()
plt.show()

x = np.linspace(0, 80, 100)
y1=func(x,pll)
y2=func(x,pr)
plt.fill_between(x,y1,y2,color=(0,0,1,0.25),label="Estimated Working Range")

plt.errorbar(distances, left, yerr=errr, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2,label = "Raw Data")
plt.errorbar(distances, right, yerr=errr, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.title('Working Range of Single Sensor Left/Right')
plt.xlabel('Distance from the Sensor (cm)')
plt.ylabel('Maximum Range Left(+)/Right(-) (cm)')
plt.legend()
plt.show()

distances1 = [0,26,36, 46, 56, 66,76,86,96,106]
high1=[0,6,7,9,10,14,15,17,21,21]
low1=[0,-6, -9, -11.5, -12.5, -14, -16, -18, -21, -25]
left1=[0,3.5,5.25,6,8,9.5,10.75,12.5,13.5,14.25]
right1=[0,-1,-2.25,-2.5,-3,-4.25,-6,-7.25,-8.75,-10]

ph1= np.polyfit(distances1,high1, deg=1)
pl1= np.polyfit(distances1,low1, deg=1)
pll1=np.polyfit(distances1,left1, deg=1)
pr1=np.polyfit(distances1,right1, deg=1)

errhl1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
errrl1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

x1 = np.linspace(0, 110, 110)
y11=func(x1,ph1)
y21=func(x1,pl1)
plt.fill_between(x1,y11,y21,color=(0,1,0,0.25))

plt.errorbar(distances1, high1, yerr=errhl1, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)
plt.errorbar(distances1, low1, yerr=errhl1, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)

x = np.linspace(0, 110, 110)
y1=func(x,ph)
y2=func(x,pl)
plt.fill_between(x,y1,y2,color=(1,0,0,0.25))

plt.errorbar(distances, high, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.errorbar(distances, low, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)

plt.title('Working Range of Single vs Three Sensor Up/Down')
plt.xlabel('Distance from the Sensor (cm)')
plt.ylabel('Maximum Range Up(+)/Down(-) (cm)')
plt.legend(["Three Sensors", "One Sensor"])
plt.show()

x1 = np.linspace(0, 110, 110)
y11=func(x,pll1)
y21=func(x,pr1)
plt.fill_between(x1,y11,y21,color=(0,1,0,0.25))

plt.errorbar(distances1, left1, yerr=errrl1, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)
plt.errorbar(distances1, right1, yerr=errrl1, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)

x = np.linspace(0, 110, 110)
y1=func(x,pll)
y2=func(x,pr)
plt.fill_between(x,y1,y2,color=(1,0,0,0.25))

plt.errorbar(distances, left, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.errorbar(distances, right, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)


plt.title('Working Range of Single vs Three Sensor Left/Right')
plt.xlabel('Distance from the Sensor (cm)')
plt.ylabel('Maximum Range Left(+)/Right(-) (cm)')
plt.legend(["Three Sensors", "One Sensor"])
plt.show()

distances2 = [0,26,36, 46, 56, 66,76]
high2=[0, 20,24,27,30,34,37]
low2=[0,-57,-73,-95,-112,-130,-143]
left2=[0, 20, 27, 34,40,47.5,53.5]
right2=[0, -11.5,-17, -23, -28.5, -33, -39.5]

ph2= np.polyfit(distances2,high2, deg=1)
pl2= np.polyfit(distances2,low2, deg=1)
pll2=np.polyfit(distances2,left2, deg=1)
pr2=np.polyfit(distances2,right2, deg=1)

err2=[0,1,1,1,2,2,2]
errr2=[0,1,1,1,1,1,1]

x1 = np.linspace(0, 110, 110)
y11=func(x1,ph1)
y21=func(x1,pl1)
plt.fill_between(x1,y11,y21,color=(0,1,0,0.25))

plt.errorbar(distances1, high1, yerr=errhl1, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)
plt.errorbar(distances1, low1, yerr=errhl1, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)

x2 = np.linspace(0, 110, 110)
y12=func(x2,ph2)
y22=func(x,pl2)
plt.fill_between(x2,y12,y22,color=(0,0,1,0.25))

plt.errorbar(distances2, high2, yerr=err2, fmt="o",c=(0,0,1,0.5),ms=4,capsize=2)
plt.errorbar(distances2, low2, yerr=err2, fmt="o",c=(0,0,1,0.5),ms=4,capsize=2)

plt.title('Working Range of Tilt vs. No Tilt Up/Down')
plt.xlabel('Distance from the Sensor (cm)')
plt.ylabel('Maximum Range Up(+)/Down(-) (cm)')
plt.legend(["No Tilt", "Tilt"])
plt.show()

x1 = np.linspace(0, 110, 110)
y11=func(x,pll1)
y21=func(x,pr1)
plt.fill_between(x1,y11,y21,color=(0,1,0,0.25))

plt.errorbar(distances1, left1, yerr=errrl1, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)
plt.errorbar(distances1, right1, yerr=errrl1, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)

x2 = np.linspace(0, 110, 110)
y12=func(x2,pll2)
y22=func(x,pr2)
plt.fill_between(x2,y12,y22,color=(0,0,1,0.25))
plt.errorbar(distances2, left2, yerr=errr2, fmt="o",c=(0,0,1,0.5),ms=4,capsize=2)
plt.errorbar(distances2, right2, yerr=errr2, fmt="o",c=(0,0,1,0.5),ms=4,capsize=2)


plt.title('Working Range of Tilt vs. No Tilt Left/Right')
plt.xlabel('Distance from the Sensor (cm)')
plt.ylabel('Maximum Range Left(+)/Right(-) (cm)')
plt.legend(["No Tilt", "Tilt"])
plt.show()


