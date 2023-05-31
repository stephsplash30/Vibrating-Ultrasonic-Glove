distances=[15,20,25,30,35,40,45,50,55,60,65]
data = [10.5,15.4,19.7,24.6,29.5,33.8,38.2,42.6, 46.6, 53.6, 56.7, 59.7, 65.5]
err = [0.1,0.1,0.1,0.2,0.2,0.2,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
plt.errorbar(distances, data, yerr=err, fmt="o",c=(1,0,0,0.5),ms=4,capsize=2)
plt.axhline(0)
plt.xlim(left=0)
plt.xlabel("Physical Distance from the Sensor (cm)")
plt.ylabel("Reported Distance from the Sensor (cm) ")
plt.title("Reported Distance vs. Physical Distance")
plt.show()