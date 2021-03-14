import matplotlib.pyplot as plt
from numpy import linspace

brzine = []
putevi = []
m = 10
F = 250
t = linspace(0, 10, 100)
a1 = []
a = F/m

for i in t:
    v = a*i
    x = v*i
    a1.append(a)
    brzine.append(v)
    putevi.append(x)

fig, axs = plt.subplots(1, 3)
axs[0].plot(t, a1)
axs[0].set(xlabel="vrijeme, t [s]", ylabel="akceleracija, a [m/s^2]")
axs[1].plot(t, brzine)
axs[1].set(xlabel="vrijeme, t [s]", ylabel="brzina, v [m/s]")
axs[2].plot(t, putevi)
axs[2].set(xlabel="vrijeme, t [s]", ylabel="put, x [m]")
axs[2].set_title("Put")
axs[0].set_title("Akceleracija")
axs[1].set_title("Brzina")
plt.show()