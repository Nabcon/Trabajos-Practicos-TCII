# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:35:08 2022

@author: Nahuel
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

N = 1000
fs = np.pi

porcentaje = 5/100

ff = np.arange(0, fs, 1/N)

H1 = 2*np.sin(ff/2)
H2 = 2*np.sin(ff)

ff_n = ff

fig, (ax1) = plt.subplots(nrows=1 , ncols=1, sharex=True)

ax1.plot(ff_n,ff, label='Derivador ideal')
ax1.plot(ff_n,H1, label= '$H_{1}(Z)$')
ax1.plot(ff_n,H2, label= '$H_{2}(Z)$')
ax1.set_xticks([0,np.pi/2, np.pi])
ax1.set_xticklabels(['0','$\Omega = \dfrac{\pi}{2} $','$\Omega = \pi $'])
ax1.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, np.pi])
ax1.set_yticklabels(['0','0.5','1','1.5','2','2.5','3','$\pi $'])
ax1.set_title("Filtro diferenciador $|H(\Omega)|$")
ax1.set_xlabel("Frecuencia Normalizada")
ax1.set_ylabel("Amplitud")
ax1.legend()
ax1.grid()

# H1
# busco el indice donde se cumple mi condicion del 5% de error
index_H1 = np.where(np.abs(ff-H1) > porcentaje)[0]
# encuentro la frecuencia normalizada en la cual se produce el 5% de error
w5_H1 = ff[index_H1]/np.pi

# H2
# Idem lo anterior, pero con H2
index_H2 = np.where(np.abs(ff-H2) > porcentaje)[0]
w5_H2 = ff[index_H2]/np.pi

# print("{:.3f}".format(w5_h1[0]),'$\pi$')
# print("{:.3f}".format(w5_h1[0]),'$\pi$')
print("{:.3f}".format(w5_H1[0]))
print("{:.3f}".format(w5_H2[0]))