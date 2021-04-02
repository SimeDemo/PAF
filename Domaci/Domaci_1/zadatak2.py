import particle as prt
import matplotlib.pyplot as plt
import numpy as np


def angle_range():
    angles = np.linspace(0, 90, 180)
    ranges = []

    for i in angles:
        p1 = prt.Particle(10, i, 0, 0)
        ranges.append(p1.range_p(0.01))

    for j in ranges:
        if j < 0.01:
            ranges.remove(j)

    return angles, ranges

def angle_duration():
    angles = np.linspace(-90, 90, 360)
    durations = []

    for i in angles:
        p1 = prt.Particle(10, i, 0, 0)
        p1.range_p(0.01)
        durations.append(p1.total_time(0.01))

    return print(durations)

angle_duration()
