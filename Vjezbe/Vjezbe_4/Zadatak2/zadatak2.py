import calculus as cal
import matplotlib.pyplot as plt
import numpy as np

def cubic(x):

    return x**3

def cubic_integrate(x):
    
    return (x**4)/4

lower0, upper0 = cal.integrate_rectangle(cubic, 0, 10, 100)
integral0 = cal.integrate_trapezoid(cubic, 0, 10, 100)
print(f"Donja i gornja meda su: {lower0} i {upper0}")
print(f"Rezultat integrala je {integral0}")

a, b = 0, 5
xlist, ylist1, ylist2, ylist3, ylist4 = [], [], [], [], []
dn = 50

for i in range(1, 20, 1):
    xlist.append(dn*i)

for x in xlist:
    lower, upper = cal.integrate_rectangle(cubic, a, b, x)
    integral_trapezoid = cal.integrate_trapezoid(cubic, a, b, x)
    integral = cubic_integrate(b) - cubic_integrate(a)

    ylist1.append(lower)
    ylist2.append(upper)
    ylist3.append(integral_trapezoid)
    ylist4.append(integral)

plt.plot(xlist,ylist1,".")
plt.plot(xlist,ylist2,".")
plt.plot(xlist,ylist3,".")
plt.plot(xlist,ylist4)
plt.xlabel("N steps")
plt.ylabel("integral")
plt.show()