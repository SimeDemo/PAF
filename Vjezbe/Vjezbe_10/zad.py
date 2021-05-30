import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import EMF as emfi


electron = emfi.EMF(np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,0]), np.array([0,0,1]), -1, 1)
x, y, z = electron.euler(20, 0.01)

electron.reset()

electron = emfi.EMF(np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,0]), np.array([0,0,1]), -1, 1)
xRK, yRK, zRK = electron.RK(20, 0.01)

positron = emfi.EMF(np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,0]), np.array([0,0,1]), 1, 1)
positron.euler(20, 0.01)

positron.electron_vs_positron(electron, positron)

electron.euler_vs_RK(x, y, z, xRK, yRK, zRK)
