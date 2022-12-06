# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:35:13 2022

@author: Nahuel
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

num_h = [1, 3, 3, 1]
den_h = [1, -2, 1.81, -0.68]

WN = int(5*10e3) # Cantidad de puntos para la funcion Freqz

w_py, h_py = sig.freqz(num_h,den_h,worN = WN)

ph_H = np.angle(h_py)

fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
ax1.plot(w_py, np.abs(h_py), label = "$Módulo |H(\Omega)|$")
ax2.plot(w_py, ph_H, label = "$Fase \\angle H(\Omega)$")
ax1.set_title("Transferencia $H(\Omega)$")# bug, alpha se pone con doble \\
ax1.set_xlabel("Frecuencia Normalizada")
ax1.set_ylabel("Amplitud")
ax2.set_xlabel("Frecuencia Normalizada")
ax2.set_ylabel("Amplitud")
ax1.set_xticks([0, 0.5, 1, 1.5, 2, 2.5, np.pi])
ax1.set_xticklabels(['0','0.5','1','1.5','2','2.5','$\Omega = \pi $'])
ax1.grid()
ax2.grid()
ax1.legend()
ax2.legend()
