import matplotlib.pyplot as plt 
import numpy as np


def fja(x1, x2, y1, y2):
    a = np.array([[x1, 1], [x2, 1]], dtype="float")
    b = np.array([y1, y2])
    solutions = np.linalg.solve(a, b)
    
    global k 
    global l

    k = solutions[0]
    l = solutions[1]
    
    if l > 0:
        return print(f"Jednadzba pravca je: y={k}x+{l}")
    else:
        return print(f"Jednadzba pravca je: y={k}x{l}")


while True:
    try:
        x1 = float(input("unesi koordinatu x1: "))
        y1 = float(input("unesi koordinatu y1: "))
        x2 = float(input("unesi koordinatu x2: "))
        y2 = float(input("unesi koordinatu y2: "))
        break
    except ValueError:
        print("netocan unos")

fja(x1, x2, y1, y2)
plt.axis("equal")
plt.plot([x1, x2], [y1, y2], "ro")

if x1 >= x2:
    x1 = round(x1)
    x = np.linspace(-x1-10, x1+10, x1*2+20)
else:
    x2 = round(x2)
    x = np.linspace(-x2-10, x2+10, x2*2+20)

y = k*x + l

plt.plot(x, y)
plt.grid()

while True:
    try:
        save = input("unesite 's' za spremanje plota u obliku pdf-a, a 'p' samo za pokazivanje plota: ")
        save = save.lower()
        if save != "s" and save != "p":
            print("netocan unos")
        elif save == "s":
            ime_plota = input("zeljeno ime filea u kojem je plot: ")
            plt.savefig(ime_plota + ".pdf")
            break
        else:
            plt.show()
            break
    except ValueError:
        print("Netocan unos")