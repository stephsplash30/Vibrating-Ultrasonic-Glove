#%% Analyse individual sensor working ranges
import matplotlib.pyplot as plt
import numpy as np

experimentinput = np.loadtxt("C:/Users/vadim/Documents/Katya/CS 15C/single_sensor_detection_range.csv", delimiter=",", skiprows=1) #read data from file
experiment = np.transpose(experimentinput)	

#top sensor
z1 = experiment[0] #get z values
zerr1 = experiment[1] #get error for z measurement
ylow1 = experiment[2] #get lower bound for y measurement 
yhigh1 = experiment[3] #get upper bound for y measurement
yerr1 = experiment[4] #get error for y measurement
xright1 = experiment[5] #get lower bound for x measurement
xleft1 = experiment[6] #get upper bound for x measurement
xerr1 = experiment[7] #get error for x measurement
#middle sensor
z2 = experiment[8] #get z values
zerr2 = experiment[9] #get error for z measurement
ylow2 = experiment[10] #get lower bound for y measurement 
yhigh2 = experiment[11] #get upper bound for y measurement
yerr2 = experiment[12] #get error for y measurement
xright2 = experiment[13] #get lower bound for x measurement
xleft2 = experiment[14] #get upper bound for x measurement
xerr2 = experiment[15] #get error for x measurement
#bottom sensor
z3 = experiment[16] #get z values
zerr3 = experiment[17] #get error for z measurement
ylow3 = experiment[18] #get lower bound for y measurement 
yhigh3 = experiment[19] #get upper bound for y measurement
yerr3 = experiment[20] #get error for y measurement
xright3 = experiment[21] #get lower bound for x measurement
xleft3 = experiment[22] #get upper bound for x measurement
xerr3 = experiment[23] #get error for x measurement

#plot ranges of each sensor for the vertical axis, concatenate upper and lower limit arrays
plt.figure(1)
plt.errorbar(np.concatenate((z1,z1), axis = 0), np.concatenate((ylow1,yhigh1), axis = 0),xerr = np.concatenate((zerr1,zerr1), axis = 0), yerr=np.concatenate((yerr1, yerr1), axis = 0), fmt="o",c=(1,0,0,0.5),ms=4,capsize=2,label="Top sensor")
plt.errorbar(np.concatenate((z2,z2), axis = 0), np.concatenate((ylow2, yhigh2), axis = 0), xerr = np.concatenate((zerr2, zerr2), axis = 0), yerr=np.concatenate((yerr2, yerr2), axis = 0), fmt="o",c=(0,1,0,0.5),ms=4,capsize=2,label="Middle sensor")
plt.errorbar(np.concatenate((z3,z3), axis = 0), np.concatenate((ylow3, yhigh3), axis = 0) ,xerr = np.concatenate((zerr3, zerr3), axis = 0), yerr=np.concatenate((yerr3, yerr3), axis = 0), fmt="o",c=(0,0,1,0.5),ms=4,capsize=2, label="Bottom sensor")
plt.xlim(left=0)
plt.title('Vertical working range of each sensor')
plt.xlabel('$Z$: distance from the sensor (cm)')
plt.ylabel('$Y$: detection range up(+)/down(-) (cm)')
plt.axhline(0)
plt.legend()
plt.show()

#plot ranges of each sensor for the horizontal axis, concatenate upper and lower limit arrays
plt.errorbar(np.concatenate((z1,z1), axis = 0), np.concatenate((xleft1,xright1), axis = 0),xerr = np.concatenate((zerr1,zerr1), axis = 0), yerr=np.concatenate((xerr1, xerr1), axis = 0), fmt="o",c=(1,0,0,0.5),ms=4,capsize=2,label="Top sensor")
plt.errorbar(np.concatenate((z2,z2), axis = 0), np.concatenate((xleft2, xright2), axis = 0), xerr = np.concatenate((zerr2, zerr2), axis = 0), yerr=np.concatenate((xerr2, xerr2), axis = 0), fmt="o",c=(0,1,0,0.5),ms=4,capsize=2,label="Middle sensor")
plt.errorbar(np.concatenate((z3,z3), axis = 0), np.concatenate((xleft3, xright3), axis = 0) ,xerr = np.concatenate((zerr3, zerr3), axis = 0), yerr=np.concatenate((xerr3, xerr3), axis = 0), fmt="o",c=(0,0,1,0.5),ms=4,capsize=2, label="Bottom sensor")
plt.xlim(left=0)
plt.title('Horizontal working range of each sensor')
plt.xlabel('$Z$: distance from the sensor (cm)')
plt.ylabel('$X$: detection range left(+)/right(-) (cm)')
plt.axhline(0)
plt.legend()
plt.show()
#%% Overlaping ranges of each sensor taken individually
experimentinput = np.loadtxt("C:/Users/vadim/Documents/Katya/CS 15C/single_sensor_detection_range_overlap.csv", delimiter=",", skiprows=1) #read data from file
experiment = np.transpose(experimentinput)	
#top sensor
z1 = experiment[0] #get z values
zerr1 = experiment[1] #get error for z measurement
ylow1 = experiment[2] #get lower bound for y measurement 
yhigh1 = experiment[3] #get upper bound for y measurement
yerr1 = experiment[4] #get error for y measurement
#middle sensor
z2 = experiment[5] #get z values
zerr2 = experiment[6] #get error for z measurement
ylow2 = experiment[7] #get lower bound for y measurement 
yhigh2 = experiment[8] #get upper bound for y measurement
yerr2 = experiment[9] #get error for y measurement
#bottom sensor
z3 = experiment[10] #get z values
zerr3 = experiment[11] #get error for z measurement
ylow3 = experiment[12] #get lower bound for y measurement 
yhigh3 = experiment[13] #get upper bound for y measurement
yerr3 = experiment[14] #get error for y measurement

#plot ranges of each sensor for the horizontal axis, concatenate upper and lower limit arrays
plt.errorbar(np.concatenate((z1,z1), axis = 0), np.concatenate((ylow1,yhigh1), axis = 0),xerr = np.concatenate((zerr1,zerr1), axis = 0), yerr=np.concatenate((yerr1, yerr1), axis = 0), fmt="o",c=(1,0,0,0.5),ms=4,capsize=2,label="Top sensor")
plt.errorbar(np.concatenate((z2,z2), axis = 0), np.concatenate((ylow2, yhigh2), axis = 0), xerr = np.concatenate((zerr2, zerr2), axis = 0), yerr=np.concatenate((yerr2, yerr2), axis = 0), fmt="o",c=(0,1,0,0.5),ms=4,capsize=2,label="Middle sensor")
plt.errorbar(np.concatenate((z3,z3), axis = 0), np.concatenate((ylow3, yhigh3), axis = 0) ,xerr = np.concatenate((zerr3, zerr3), axis = 0), yerr=np.concatenate((yerr3, yerr3), axis = 0), fmt="o",c=(0,0,1,0.5),ms=4,capsize=2, label="Bottom sensor")
plt.xlim(left=0)
plt.title('Vertical working range of each sensor overlapped')
plt.xlabel('$Z$: distance from the sensor (cm)')
plt.ylabel('$Y$: detection range up(+)/down(-) (cm)')
plt.axhline(0)
plt.legend()
plt.show()


#%% Analyse vibration model and measurement acuracy
import matplotlib.pyplot as plt
import numpy as np
import math

experimentinput = np.loadtxt("C:/Users/vadim/Documents/Katya/CS 15C/distance_power.csv", delimiter=",", skiprows=1) #read data from file
experiment = np.transpose(experimentinput)	

z =  experiment[0] #get z values
zerr = experiment[1] #get error for z measurement
data1 = experiment[2]
err1 = experiment[3] 
data2 = experiment[4] 
err2 = experiment[5] 

for i in range(len(data2)):
    data2[i]*=0.033
#plt.errorbar(distances, data1, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
#plt.axhline(0)
#plt.xlim(left=0)
#plt.xlabel("Physical Distance from the Sensor (cm)")
#plt.ylabel("Reported Distance from the Sensor (cm) ")
#plt.title("Reported Distance vs. Physical Distance")
#plt.show()

x = np.linspace(0, 75, 100)

#create a function for the vibration model
def func(x):
    return np.where((x < 30) & (x >= 0), 1.65, 0.033*50 * np.exp(-(x - 30) / 40))

# Create the figure and the first y-axis
fig, ax1 = plt.subplots()
ax1.errorbar(z, data1, xerr = zerr, yerr=err1, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
ax1.axline((0,0), slope=1, c=(0,0,1,0.5))
ax1.set_xlabel('Physical Distance from the Sensor (cm)')
ax1.set_ylabel('Reported Distance from the Sensor (cm)', color='r')
ax1.set_ylim((0,70))

# Create the second y-axis
ax2 = ax1.twinx()
ax2.errorbar(z, data2, xerr= zerr, yerr=err2, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)
ax2.plot(x,func(x),c=(0,0,1,0.5))
ax2.set_ylabel('Voltage from the PWM Output (V)', color='g')
ax2.set_ylim((0,2))

# Customize the appearance
ax1.tick_params(axis='y', colors='r')
ax2.tick_params(axis='y', colors='g')

plt.title("Voltage Output and Reported Distance vs. Physical Distance")

# Show the plot
plt.show()

#%% plot sensor range in 3D 
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

experimentinput = np.loadtxt("C:/Users/vadim/Documents/Katya/CS 15C/single_sensor_detection_range.csv", delimiter=",", skiprows=1)
experiment = np.transpose(experimentinput)	 	
#z - 0 degree tilt measurement		
z = experiment[0]
zErr = experiment[1]
yLow = experiment[2]
yHigh = experiment[3]
yErr = experiment[4]
xRight = experiment[5]
xLeft = experiment[6]
xErr = experiment[7]

data = []
#scatterplot of all the data with errorbars
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(xRight,yLow,z, color = "#4642c7", s = 0.5)
line1 = []
for i in np.arange(0, len(z)):
    ax.plot([xRight[i]+xErr[i], xRight[i]-xErr[i]], [yLow[i], yLow[i]], [z[i], z[i]], color = "#4642c7", marker="_")
    ax.plot([xRight[i], xRight[i]], [yLow[i]+yErr[i], yLow[i]-yErr[i]], [z[i], z[i]],color = '#4642c7', marker="_")
    ax.plot([xRight[i], xRight[i]], [yLow[i], yLow[i]], [z[i]+zErr[i], z[i]-zErr[i]], color = '#4642c7', marker="_")
    data.append([xRight[i], yLow[i], z[i]])
    line1.append([xRight[i], yLow[i], z[i]])
    
ax.scatter(xLeft,yLow,z, color = "#4642c7", s = 0.5)
line2 = []
for i in np.arange(0, len(z)):
    ax.plot([xLeft[i]+xErr[i], xLeft[i]-xErr[i]], [yLow[i], yLow[i]], [z[i], z[i]], color = "#4642c7", marker="_")
    ax.plot([xLeft[i], xLeft[i]], [yLow[i]+yErr[i], yLow[i]-yErr[i]], [z[i], z[i]],color = '#4642c7', marker="_")
    ax.plot([xLeft[i], xLeft[i]], [yLow[i], yLow[i]], [z[i]+zErr[i], z[i]-zErr[i]], color = '#4642c7', marker="_")
    data.append([xLeft[i], yLow[i], z[i]])
    line2.append([xLeft[i], yLow[i], z[i]])
    
ax.scatter(xRight,yHigh,z, color = "#4642c7", s = 0.5)
line3 = []
for i in np.arange(0, len(z)):
    ax.plot([xRight[i]+xErr[i], xRight[i]-xErr[i]], [yHigh[i], yHigh[i]], [z[i], z[i]], color = "#4642c7", marker="_")
    ax.plot([xRight[i], xRight[i]], [yHigh[i]+yErr[i], yHigh[i]-yErr[i]], [z[i], z[i]],color = '#4642c7', marker="_")
    ax.plot([xRight[i], xRight[i]], [yHigh[i], yHigh[i]], [z[i]+zErr[i], z[i]-zErr[i]], color = '#4642c7', marker="_")
    data.append([xRight[i], yHigh[i], z[i]])
    line3.append([xRight[i], yHigh[i], z[i]])

ax.scatter(xLeft,yHigh,z, color = "#4642c7", s = 0.5)
line4 = []
for i in np.arange(0, len(z)):
    ax.plot([xLeft[i]+xErr[i], xLeft[i]-xErr[i]], [yHigh[i], yHigh[i]], [z[i], z[i]], color = "#4642c7", marker="_")
    ax.plot([xLeft[i], xLeft[i]], [yHigh[i]+yErr[i], yHigh[i]-yErr[i]], [z[i], z[i]],color = '#4642c7', marker="_")
    ax.plot([xLeft[i], xLeft[i]], [yHigh[i], yHigh[i]], [z[i]+zErr[i], z[i]-zErr[i]], color = '#4642c7', marker="_")
    data.append([xLeft[i], yHigh[i], z[i]])
    line4.append([xLeft[i], yHigh[i], z[i]])

#draw the mount
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

# vertices of the shape
v = np.array([[23, 29, -34], [-23, 29, -34], [23, 29, 4], [-23, 29, 4],  [23, -25, -16], [-23, -25, -16], [23, -25, -34], [-23, -25, -34], [23,9,4], [-23,9,4], [23,-9,-4], [-23,-9,-4] ])
v = np.divide(v,10)
ax.scatter(v[:, 0], v[:, 1], v[:, 2], marker = "None")

#generate list of sides' polygons of the shape
verts = [[v[0],v[1], v[3], v[2]], [v[3], v[2], v[8], v[9]], [v[0], v[1], v[7], v[6]], [v[7], v[6], v[4], v[5]], [v[4], v[5], v[11], v[10]], [v[11], v[10], v[8], v[9]], [v[2],v[0], v[6], v[4], v[10], v[8]], [v[3],v[1], v[7], v[5], v[11], v[9]]]

#plot sides
ax.add_collection3d(Poly3DCollection(verts, 
facecolors='#912e27', linewidths=1, edgecolors='#75241e', alpha=.75))
ax.set_xlabel('$X$', linespacing=0.01)
ax.set_ylabel('$Y$', linespacing=0.01)
ax.set_zlabel('$Z$', linespacing=0.01)

#orient the view window 
ax.view_init(270,0, vertical_axis='x')
ax.view_init(40,90, vertical_axis='y')
#ax.view_init(270,0, vertical_axis='x')
ax.xaxis.gridlines.set_lw(0.05)
ax.yaxis.gridlines.set_lw(0.05)
ax.zaxis.gridlines.set_lw(0.05)
ax.xaxis.set_tick_params(labelsize=7)
ax.yaxis.set_tick_params(labelsize=7)
ax.zaxis.set_tick_params(labelsize=7)

#create X,Y,Z point array for the first line
pts = []
X = []
Y = []
Z = []    

#sort the data array to put in x,y,z values in the correct order
for i in range(len(line1)):
    for j in range(len(line1[0])):
        if j == 0:
            X.append(line1[i][j])
        if j == 1:
            Y.append(line1[i][j])
        if j == 2:
            Z.append(line1[i][j])

#define a linear function for a fit
def func(t, a, b):
    return a*t + b

#create a parameter for the linear parametric equation and find the appropriate coefficients
t = np.linspace(0, 100, 5)
tt = np.linspace(0,100, 200)
poptx, pcovx = optimize.curve_fit(func, t, X, maxfev=1000)
popty, pcovy = optimize.curve_fit(func, t, Y, maxfev=1000)
poptz, pcovz = optimize.curve_fit(func, t, Z, maxfev=1000)
#plot the parametric curves
ax.plot(func(tt,*poptx), func(tt, *popty), func(tt, *poptz), 'r')
pts.append([func(0,*poptx), func(0, *popty), func(0, *poptz)])
pts.append([func(100,*poptx), func(100, *popty), func(100, *poptz)])

#create X,Y,Z point array for the second line, override the previous x,y,z values
X = []
Y = []
Z = []    

for i in range(len(line2)):
    for j in range(len(line2[0])):
        if j == 0:
            X.append(line2[i][j])
        if j == 1:
            Y.append(line2[i][j])
        if j == 2:
            Z.append(line2[i][j])
            
#create a parameter for the linear parametric equation and find the appropriate coefficients
poptx, pcovx = optimize.curve_fit(func, t, X, maxfev=1000)
popty, pcovy = optimize.curve_fit(func, t, Y, maxfev=1000)
poptz, pcovz = optimize.curve_fit(func, t, Z, maxfev=1000)
#plot the parametric curves
ax.plot(func(tt,*poptx), func(tt, *popty), func(tt, *poptz), 'r')
pts.append([func(0,*poptx), func(0, *popty), func(0, *poptz)])
pts.append([func(100,*poptx), func(100, *popty), func(100, *poptz)])

#create X,Y,Z point array for the third line, override the previous x,y,z values
X = []
Y = []
Z = []    

for i in range(len(line3)):
    for j in range(len(line3[0])):
        if j == 0:
            X.append(line3[i][j])
        if j == 1:
            Y.append(line3[i][j])
        if j == 2:
            Z.append(line3[i][j])

poptx, pcovx = optimize.curve_fit(func, t, X, maxfev=1000)
popty, pcovy = optimize.curve_fit(func, t, Y, maxfev=1000)
poptz, pcovz = optimize.curve_fit(func, t, Z, maxfev=1000)

ax.plot(func(tt,*poptx), func(tt, *popty), func(tt, *poptz), 'r')
pts.append([func(0,*poptx), func(0, *popty), func(0, *poptz)])
pts.append([func(100,*poptx), func(100, *popty), func(100, *poptz)])

#create X,Y,Z point array for the fourth line, override the previous x,y,z values
X = []
Y = []
Z = []    

for i in range(len(line4)):
    for j in range(len(line4[0])):
        if j == 0:
            X.append(line4[i][j])
        if j == 1:
            Y.append(line4[i][j])
        if j == 2:
            Z.append(line4[i][j])

poptx, pcovx = optimize.curve_fit(func, t, X, maxfev=1000)
popty, pcovy = optimize.curve_fit(func, t, Y, maxfev=1000)
poptz, pcovz = optimize.curve_fit(func, t, Z, maxfev=1000)

ax.plot(func(tt,*poptx), func(tt, *popty), func(tt, *poptz), 'r')
pts.append([func(0,*poptx), func(0, *popty), func(0, *poptz)])
pts.append([func(100,*poptx), func(100, *popty), func(100, *poptz)])


verts = [[pts[0], pts[2], pts[3], pts[1]], [pts[4], pts[5], pts[7], pts[6]],  [pts[4], pts[5], pts[1], pts[0]],  [pts[6], pts[7], pts[3], pts[2]] ]
#plot sides
ax.add_collection3d(Poly3DCollection(verts, 
facecolors='#3e30fc', linewidths=1, alpha=.25))

plt.show()

#%% Analyse working range of a single sensor
import matplotlib.pyplot as plt
import numpy as np

experimentinput = np.loadtxt("C:/Users/vadim/Documents/Katya/CS 15C/single_sensor_detection_range.csv", delimiter=",", skiprows=1) #read data from file
experiment = np.transpose(experimentinput)	
 	
z = experiment[0] #get z values
zerr = experiment[1] #get error for z measurement
ylow = experiment[2] #get lower bound for y measurement 
yhigh = experiment[3] #get upper bound for y measurement
yerr = experiment[4] #get error for y measurement
xright = experiment[5] #get lower bound for x measurement
xleft = experiment[6] #get upper bound for x measurement
xerr = experiment[7] #get error for x measurement

#fit the data to a linear relationship between z and x,  z and y separately for the upper and lower bound
yh= np.polyfit(z, yhigh, deg=1) 
yl= np.polyfit(z, ylow, deg=1)
xl=np.polyfit(z, xleft, deg=1)
xr=np.polyfit(z, xright, deg=1)

#define a linear function to plot the best fit line
def func(x, p):
    return p[0]*x+p[1]

#get x and y points to use for the best fit line
x = np.linspace(0, 80, 100)
y1=func(x,yh)
y2=func(x,yl)
y3=func(x,xl)
y4=func(x,xr)

#shade the area between two best fit lines to indicate the approximate detection range of the sensor
plt.fill_between(x,y1,y2,color=(0,0,1,0.25),label="Estimated sensing range")
#make a scatterplot with errorbars of the z and y relationship for both the upper and lower bound
plt.errorbar(z, yhigh, xerr = zerr, yerr = yerr, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2, label = "Raw data")
plt.errorbar(z, ylow, xerr = zerr, yerr = yerr, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.title('Vertical working range of a single sensor')
plt.xlabel('$Z$: distance from the sensor (cm)')
plt.ylabel('$Y$: detection range up(+)/down(-) (cm)')
plt.legend()
plt.show()

#shade the area between two best fit lines to indicate the approximate detection range of the sensor
plt.fill_between(x,y3,y4,color=(0,0,1,0.25), label = "Estimated sensing range")
#make a scatterplot with errorbars of the z and x relationship for both the upper and lower bound
plt.errorbar(z, xleft, xerr= xerr, yerr=yerr, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2,label = "Raw data")
plt.errorbar(z, xright, xerr = xerr, yerr=yerr, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.title('Horizontal working range of a single sensor')
plt.xlabel('$Z$: distance from the sensor (cm)')
plt.ylabel('$X$: detection range left(+)/right(-) (cm)')
plt.legend()
plt.show()
#%% Compare working range of three sensors with the working range of a single sensor
experimentinput = np.loadtxt("C:/Users/vadim/Documents/Katya/CS 15C/device_detection_range.csv", delimiter=",", skiprows=1) #read data from file
experiment = np.transpose(experimentinput)	

 	
z3 = experiment[0] #get z values, 3 in the end stands for 3 sensors together
zerr3 = experiment[1] #get error for z measurement
ylow3 = experiment[2] #get lower bound for y measurement 
yhigh3 = experiment[3] #get upper bound for y measurement
yerr3 = experiment[4] #get error for y measurement
xright3 = experiment[5] #get lower bound for x measurement
xleft3 = experiment[6] #get upper bound for x measurement
xerr3 = experiment[7] #get error for x measurement

#fit the data to a linear relationship between z and x,  z and y separately for the upper and lower bound
yh3= np.polyfit(z3, yhigh3, deg=1) 
yl3= np.polyfit(z3, ylow3, deg=1)
xl3=np.polyfit(z3, xleft3, deg=1)
xr3=np.polyfit(z3, xright3, deg=1)

#get x and y points to use for the best fit line for the whole device
x3 = np.linspace(0, 110, 110)
y13=func(x3,yh3)
y23=func(x3,yl3)
y33=func(x3,xl3)
y43=func(x3,xr3)
#change the size of x and y arrays for one sensor used for the best fit line
y1=func(x3,yh)
y2=func(x3,yl)
y3=func(x3,xl)
y4=func(x3,xr)

#shade the area between two best fit lines to indicate the approximate detection range of the sensor
plt.fill_between(x3,y13,y23,color=(0,1,0,0.25),label="Whole device") #- estimated sensing range")
#make a scatterplot with errorbars of the z and y relationship for both the upper and lower bound, whole device
plt.errorbar(z3, yhigh3, xerr= xerr3, yerr=yerr3, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2) #  label = "Whole device - raw data")
plt.errorbar(z3, ylow3, xerr = xerr3, yerr=yerr3, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)

#shade the area between two best fit lines to indicate the approximate detection range of the sensor
plt.fill_between(x3,y1,y2,color=(1,0,0,0.25),label="Single sensor")# - estimated sensing range")
#make a scatterplot with errorbars of the z and y relationship for both the upper and lower bound, single sensor 
plt.errorbar(z, yhigh, xerr = xerr, yerr=yerr, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)#label = "Single sensor - raw data")
plt.errorbar(z, ylow, xerr = xerr, yerr=yerr, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)

plt.title('Comparison of whole device and single sensor vertical sensing ranges')
plt.xlabel('$Z$: distance from the sensor (cm)')
plt.ylabel('$Y$: detection range up(+)/down(-) (cm)')
plt.legend()
plt.show()

#shade the area between two best fit lines to indicate the approximate detection range of the sensor
plt.fill_between(x3[10:],y33[10:],y43[10:],color=(0,1,0,0.25), label = "Whole device")
#make a scatterplot with errorbars of the z and y relationship for both the upper and lower bound, whole device
plt.errorbar(z3, xleft3, xerr= xerr3, yerr=yerr3, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2) #  label = "Whole device - raw data")
plt.errorbar(z3, xright3, xerr = xerr3, yerr=yerr3, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)

#shade the area between two best fit lines to indicate the approximate detection range of the sensor
plt.fill_between(x3,y3,y4,color=(1,0,0,0.25), label = "Single sensor")
#make a scatterplot with errorbars of the z and y relationship for both the upper and lower bound, single sensor 
plt.errorbar(z, xleft, xerr = xerr, yerr=yerr, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)#label = "Single sensor - raw data")
plt.errorbar(z, xright, xerr = xerr, yerr=yerr, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)

plt.title('Comparison of whole device and single sensor horizontal sensing ranges')
plt.xlabel('$Z$: distance from the sensor (cm)')
plt.ylabel('$X$: detection range left(+)/right(-) (cm)')
plt.legend()
plt.show()
#%% Compare working range of the whole device with the test rod arbitrarily tilted and facing the device straight (not tilted)
experimentinput = np.loadtxt("C:/Users/vadim/Documents/Katya/CS 15C/device_detection_range_wide.csv", delimiter=",", skiprows=1) #read data from file
experiment = np.transpose(experimentinput)	

z3_ = experiment[0] #get z values, 3 in the end stands for 3 sensors together, dash in the end stands for "wide range"
zerr3_ = experiment[1] #get error for z measurement
ylow3_ = experiment[2] #get lower bound for y measurement 
yhigh3_ = experiment[3] #get upper bound for y measurement
yerr3_ = experiment[4] #get error for y measurement
xright3_ = experiment[5] #get lower bound for x measurement
xleft3_ = experiment[6] #get upper bound for x measurement
xerr3_ = experiment[7] #get error for x measurement

#fit the data to a linear relationship between z and x,  z and y separately for the upper and lower bound
yh3_= np.polyfit(z3_, yhigh3_, deg=1) 
yl3_= np.polyfit(z3_, ylow3_, deg=1)
xl3_=np.polyfit(z3_, xleft3_, deg=1)
xr3_=np.polyfit(z3_, xright3_, deg=1)

#get x and y points to use for the best fit line for the whole device
y13_=func(x3,yh3_)
y23_=func(x3,yl3_)
y33_=func(x3,xl3_)
y43_=func(x3,xr3_)

#shade the area between two best fit lines to indicate the approximate detection range of the sensor
plt.fill_between(x3,y13_,y23_,color=(0,1,0,0.25),label="Arbitrary tilt") #- estimated sensing range")
#make a scatterplot with errorbars of the z and y relationship for both the upper and lower bound, whole device
plt.errorbar(z3_, yhigh3_, xerr= xerr3_, yerr=yerr3_, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2) #  label = "arbitrary tilt - raw data")
plt.errorbar(z3_, ylow3_, xerr = xerr3_, yerr=yerr3_, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)

#shade the area between two best fit lines to indicate the approximate detection range of the sensor
plt.fill_between(x3,y13,y23,color=(1,0,0,0.25),label="No tilt")# - estimated sensing range")
#make a scatterplot with errorbars of the z and y relationship for both the upper and lower bound, single sensor 
plt.errorbar(z3, yhigh3, xerr = xerr3, yerr=yerr3, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)#label = "no tilt - raw data")
plt.errorbar(z3, ylow3, xerr = xerr3, yerr=yerr3, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)

plt.title('Comparison of the device vertical sensing ranges when the test rod is facing \n the device directly and when it is being arbitrarily tilted', fontsize = 10)
plt.xlabel('$Z$: distance from the sensor (cm)')
plt.ylabel('$Y$: detection range up(+)/down(-) (cm)')
plt.legend()
plt.show()

#shade the area between two best fit lines to indicate the approximate detection range of the sensor
plt.fill_between(x3[10:],y33[10:],y43[10:],color=(1,0,0,0.25), label = "No tilt")
#make a scatterplot with errorbars of the z and y relationship for both the upper and lower bound, whole device
plt.errorbar(z3, xleft3, xerr= xerr3, yerr=yerr3, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2) #  label = "No tilt - raw data")
plt.errorbar(z3, xright3, xerr = xerr3, yerr=yerr3, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)

#shade the area between two best fit lines to indicate the approximate detection range of the sensor
plt.fill_between(x3,y33_,y43_,color=(0,1,0,0.25), label = "Arbitrary tilt")
#make a scatterplot with errorbars of the z and y relationship for both the upper and lower bound, single sensor 
plt.errorbar(z3_, xleft3_, xerr = xerr3_, yerr=yerr3_, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)#label = "Arbitrary tilt - raw data")
plt.errorbar(z3_, xright3_, xerr = xerr3_, yerr=yerr3_, fmt="o",c=(0,1,0,0.5),ms=4,capsize=2)

plt.title('Comparison of the device horizontal sensing ranges when the test rod is facing \n the device directly and when it is being arbitrarily tilted', fontsize = 10)
plt.xlabel('$Z$: distance from the sensor (cm)')
plt.ylabel('$X$: detection range left(+)/right(-) (cm)')
plt.legend()
plt.show()
