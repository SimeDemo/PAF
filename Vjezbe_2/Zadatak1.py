import matplotlib.pyplot as plt
from numpy import linspace

brzine = []
putevi = []
m = 10
F = 250
dt = 0.1
a1 = []
v = [0]
x = [0]
t = []
a = F/m
counter = -1 

for i in range(100):
    counter += 1
    v.append(v[counter] + a*dt)
    x.append(x[counter] + v[counter]*dt)
    a1.append(a)
    t.append(dt*i)

v.pop(0)
x.pop(0)

fig, axs = plt.subplots(1, 3)
axs[0].plot(t, a1)
axs[0].set(xlabel="vrijeme, t [s]", ylabel="akceleracija, a [m/s^2]")
axs[1].plot(t, v)
axs[1].set(xlabel="vrijeme, t [s]", ylabel="brzina, v [m/s]")
axs[2].plot(t, x)
axs[2].set(xlabel="vrijeme, t [s]", ylabel="put, x [m]")
axs[0].set_title("Akceleracija")
axs[1].set_title("Brzina")
axs[2].set_title("Put")
plt.show()
