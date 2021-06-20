import matplotlib.pyplot as plt
import harmonic_oscillator as ho
import numpy as np


ho1 = ho.HarmonicOscillator(10, 5, 5, 5, 50)

ho1_period = ho1.cal_period(0.001)

print(f"period je {ho1_period}s")

ho2 = ho.HarmonicOscillator(11, 7, 5, -4, 50)

xlist, ylist = [], []
dt, k, n = 0.2, 1.1, 60

for i in range(n):
    num = ho2.cal_period(dt)
    analitic = ho2.cal_period_analitical()
    error = (abs(num - analitic) / analitic) * 100
    xlist.append(dt)
    ylist.append(error)
    dt = dt/k

plt.plot(xlist,ylist)
plt.xlabel("dt [s]")
plt.ylabel("error [%]")
plt.xscale("log")
plt.show()