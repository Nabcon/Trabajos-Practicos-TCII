# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:52:20 2022

@author: Nahuel
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig


#%% D) Integrador con perdidas 
alfa = 0.9

num_h = [alfa, 0]
den_h = [1, -(1-alfa)]

WN = int(5*10e3) # Cantidad de puntos para la funcion Freqz

w_py, h_py = sig.freqz(num_h,den_h,worN = WN)

ph_H = np.angle(h_py)

fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
ax1.plot(w_py, np.abs(h_py), label = "Módulo")
ax2.plot(w_py, ph_H, label = "Fase")
ax1.set_title("Integrador con perdidas - $\\alpha$ = 0.9")# bug, alpha se pone con doble \\
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

#%% E) 

alfa = 0.9
W_0 = np.pi/10 # frecuencia de interes

num_h = [1, -1]
den_h = [1, -alfa]

WN = int(5*10e3) # Cantidad de puntos para la funcion Freqz

w_py, h_py = sig.freqz(num_h,den_h,worN = WN)

h_py_v = np.abs(h_py)
h_py_db = 20*np.log10(np.maximum(np.abs(h_py), 1e-4))
ph_H = np.angle(h_py)
ph_H[0] = np.pi/2

# plot
fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
ax1.plot(w_py, h_py_db, label = "Módulo")
ax2.plot(w_py, ph_H, label = "Fase")
ax1.set_title("Filtro elimina continua - $\\alpha$ = 0.9")# bug, alpha se pone con doble \\
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

#%% parte 2
index_w01 = np.where(w_py > W_0)[0] # me guardo el index donde la frecuencia es 0.1Pi
# nunca toco los extremos de alfa=1 y alfa=0
K = np.linspace(0.99,0.01,num=99) #inicio, final, numero de puntos intermedios

for i in K:
    num_h = [1, -1]
    den_h = [1, -i]
    w_py, h_py = sig.freqz(num_h,den_h,worN = WN)
    h_py_db = 20*np.log10(np.maximum(np.abs(h_py), 1e-4))
    
    # si hay 3db de diferencia, mostrama el k
    if(h_py_db[-1] - h_py_db[index_w01[0]] > 3):
        print(h_py_db[-1] - h_py_db[index_w01[0]])
        print("El alfa que da -3dB en la frecuencia elegida es:",i)
        break

fig, (ax1) = plt.subplots(nrows=1 , ncols=1, sharex=True)

ax1.plot(w_py,h_py_db, label= '$\\alpha$  = {:.2}'.format(i))
ax1.set_xticks([0, np.pi/10, 0.5, 1, 1.5, 2, 2.5, np.pi])
ax1.set_xticklabels(['0','$\Omega = 0,1\pi$','0.5','1','1.5','2','2.5','$\Omega = \pi $'])
ax1.set_title("Filtro elimina continua $|H(\Omega)|dB$")
ax1.set_xlabel("Frecuencia Normalizada")
ax1.set_ylabel("Amplitud")
ax1.legend()
ax1.grid()


