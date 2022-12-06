import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

#Datos
Rv = 10e6
Ri = np.arange(0,10e6)

#Error de metodo Tension Bien medida
emTBM = -(Ri/Rv)*100

plt.plot(Ri,emTBM)