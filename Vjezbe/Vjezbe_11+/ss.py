import Universe as uni
import numpy as np
import matplotlib.pyplot as plt

au, day = 1.496e11, 60*60*24
year = 365.242 * day

sun = uni.Planet(1.989e30, np.array([0,0]), np.array([0,0]))
mercury = uni.Planet(3.3e24, np.array([0,0.466*au]), np.array([-47362,0]))
venus = uni.Planet(4.8685e24, np.array([0.723*au,0]), np.array([0,35020]))
earth = uni.Planet(5.9742e24, np.array([-au,0]), np.array([0,29783]))
mars = uni.Planet(6.417e23, np.array([0,-1.666*au]), np.array([24007,0]))

ss = uni.Universe()

ss.create(sun)
ss.create(mercury)
ss.create(venus)
ss.create(earth)
ss.create(mars)

ss.evolve(5 * year, day)

fig = plt.figure(figsize=(10, 10))

plt.plot(sun.xcoords, sun.ycoords, label="Sun", color="yellow", linewidth=5.0)

plt.plot(mercury.xcoords, mercury.ycoords, label="Mercury", color="orange")
plt.plot(mercury.xcoords[-1], mercury.ycoords[-1], 'o', color="orange")

plt.plot(venus.xcoords, venus.ycoords, label="Venus", color="red")
plt.plot(venus.xcoords[-1], venus.ycoords[-1], 'o', color="red")

plt.plot(earth.xcoords, earth.ycoords, label="Earth", color="blue")
plt.plot(earth.xcoords[-1], earth.ycoords[-1], 'o', color="blue")

plt.plot(mars.xcoords, mars.ycoords, label="Mars", color="brown")
plt.plot(mars.xcoords[-1], mars.ycoords[-1], 'o', color="brown")

plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.savefig("solar_system")
plt.show()