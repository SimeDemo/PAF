import particle as prt
import numpy as np 
import matplotlib.pyplot as plt


def error_graph():

    p1 = prt.Particle(10, 60, 0, 0) 
    dt_range = np.linspace(0.1, 0.0001, 10000)
    errors = []
    analy = p1.analytically()

    for i in dt_range:
        p1.reset()
        p1 = prt.Particle(10, 60, 0, 0)
        errors.append((abs(analy - p1.range_p(i)) / analy) * 100)
    
    plt.plot(dt_range, errors)
    plt.xlabel("dt [s]")
    plt.ylabel("absolute relative error [%]")
    plt.title("absolute relative error for range of projectile")
    plt.show()

error_graph()
