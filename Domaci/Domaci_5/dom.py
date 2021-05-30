import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import EMF as emfi

def constantF(t):

    Bx, By, Bz = 0, 0, 1

    return np.array((Bx,By,Bz))


def time_varyingF(t):

    Bx, By, Bz = 0, 0, t / 10

    return np.array((Bx,By,Bz))


electron = emfi.EMF(np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,0]), np.array([0,0,1]), -1, 1, constantF)
x, y, z = electron.euler(10, 0.01)

electron.reset()

electron = emfi.EMF(np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,0]), np.array([0,0,1]), -1, 1, time_varyingF)
xTV, yTV, zTV = electron.euler(10, 0.01)

electron.const_vs_TV(x, y, z, xTV, yTV, zTV)

positron = emfi.EMF(np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,0]), np.array([0,0,1]), 1, 1, time_varyingF)
xP, yP, zP = positron.euler(20, 0.01)

positron.electron_vs_positron_TV(xTV, yTV, zTV, xP, yP, zP)