import math
import numpy as np
import matplotlib.pyplot as plt

def roxy(x, y, ox, oy, r):
        #crtanje kruznice i tocke
    ax = plt.gca()
    ax.cla()
    kruznica = plt.Circle((ox, oy), r, color="b", fill=False)
    ax.set_ylim(-10, 10)
    ax.set_xlim(-10, 10)
    ax.add_patch(kruznica)
    plt.plot([x], [y], "ro")
    
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

    d = math.sqrt((x-ox)**2 + (y-oy)**2)
    if d < r:
        return print(f"\nKoordinate tocke: {x, y}\nUdaljenost do kruznice: {d}\ntocka je unutar kruznice\n")
    elif d == r:
        return print(f"\nKoordinate tocke: {x, y}\nUdaljenost do kruznice: {d}\ntocka je na kruznici\n")
    else:
        return print(f"\nKoordinate tocke: {x, y}\nUdaljenost do kruznice: {d}\ntocka je izvan kruznice\n")


while True:
    try:
        x = float(input("unesi koordinatu x: "))
        y = float(input("unesi koordinatu y: "))
        ox = float(input("unesi koordinatu ishodista ox: "))
        oy = float(input("unesi koordinatu ishodista oy: "))
        r = float(input("unesi radijus kruznice r: "))
        break
    except ValueError:
        print("netocan unos")

roxy(x, y, ox, oy, r)