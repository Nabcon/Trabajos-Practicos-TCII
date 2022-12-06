# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:45:15 2022

@author: Nahuel
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

def TS9_funcion(fc, fs,xlim1=0, xlim2=10,ylim1=-60, ylim2=4):
    
    WN = int(5*10e3) # Cantidad de puntos para la funcion Freqz
    KHz = 1000
    # Frecuencia de corte del filtro
    # fc = 1e3
    W_fc = 2*np.pi*fc
    # Frecuencia de Sampling
    # fs = 100e3
    nq = fs/2
    ws = 2*np.pi*fs
    
    # Normalizacion de las Fs
    fs_n = fs/W_fc
    ws_n = ws/W_fc
    
    # K de transormada Bilineal
    K = 2*fs_n
    # K = np.pi/(2*np.tan(np.pi*(fc/fs)))
    # Q de Butter Orden 2
    Q = np.sqrt(2)/2
    
    # Coeficientes desnormalizados
    A0 = K**2 + K/Q + 1
    A1 = 2 - 2*K**2
    A2 = K**2 - K/Q + 1
    
    B0 = 1
    B1 = 2
    B2 = 1
    
    #Coeficientes normalizados
    a0 = A0/A0
    a1 = A1/A0
    a2 = A2/A0
    
    b0 = B0/A0
    b1 = B1/A0
    b2 = B2/A0
    
    numz = [b0, b1, b2]
    denz = [a0, a1, a2]
    
    w, h = sig.freqz(numz,denz,WN)
    
    # simulacion python
    num_lp = [0,  0,  1]
    den_lp = [1, 1/Q, 1]
    
    numz_py, denz_py = sig.bilinear(num_lp, den_lp, fs_n) 
    w_py, h_py = sig.freqz(numz_py,denz_py,WN)
    
    # filtro analogico
    # w_analog, h_analog = sig.freqs(num_lp,den_lp)
    w_analog, h_analog = sig.freqs(num_lp,den_lp,  worN=np.logspace(-3, 2, 1000))
    h_analog_db    = 20*np.log10(np.maximum(np.abs(h_analog), 1e-4))
    
    h_db    = 20*np.log10(np.maximum(np.abs(h), 1e-4))
    h_db_py = 20*np.log10(np.maximum(np.abs(h_py), 1e-4))
    
    # Grafico
    fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True)
    # MODULO
    fig.suptitle('ButterWorth N=2')
    ax.plot(w*nq/(np.pi*KHz), h_db, label = 'Calculado')
    ax.plot(w_py*nq/(np.pi*KHz), h_db_py,color='purple',linestyle='dashed', label = 'Python')
    ax.plot(w_analog*fc/KHz, h_analog_db, color = 'orange',linestyle=':',  linewidth=3, label = 'Analogico')
    ax.grid(True)
    ax.set_title('Respuesta Magnitud $f_c = {} KHz$ | $f_s = {} KHz$'.format(fc/KHz, fs/KHz))
    ax.set_ylabel('Magnitud [dB]')
    ax.set_xlabel('Frecuencia [KHz]')
    ax.legend()
    ax.set_xlim([xlim1, xlim2])
    ax.set_ylim([ylim1, ylim2])
    
    # # descomentar para ver los graficos en la frecuencia de corte
    
    # # atenuacion 3db en fc = 1KHz
    # ax.set_xlim([0, 2])
    # ax.set_ylim([-14, 3])
    # ax.set_xticks([0, 0.5, 1, 1.5, 2])
    # ax.set_xticklabels(['0', '0.5','$f_c = 1$','1.5','2'])
    # ax.set_yticks([-12, -9, -6, -3, 0, 3])

fc = 1e3
fs = 100e3

TS9_funcion(fc, fs,0,2,-6,1)
#%% B) Reducimos la frecuencia de muestreo a 10KHz 
fc = 1e3
fs = 10e3
TS9_funcion(fc, fs,0,2,-5,1)

#%% C).A Cambiamos la frecuencia de corte a 6KHz - fs = 100KHz

def TS8_funcion_c(fc, fs,num,den,xlim1=0, xlim2=10,ylim1=-60, ylim2=4):
    
    WN = int(5*10e3) # Cantidad de puntos para la funcion Freqz
    KHz = 1000
    # Frecuencia de corte del filtro
    # fc = 1e3
    W_fc = 2*np.pi*fc
    # Frecuencia de Sampling
    # fs = 100e3
    nq = fs/2
    
    # Normalizacion de las Fs
    fs_n = fs/W_fc

    numz_py, denz_py = sig.bilinear(num, den, fs_n) 
    w_py, h_py = sig.freqz(numz_py,denz_py,WN)
    
    # filtro analogico
    # w_analog, h_analog = sig.freqs(num_lp,den_lp)
    w_analog, h_analog = sig.freqs(num,den,  worN=np.logspace(-3, 2, 1000))
    h_analog_db    = 20*np.log10(np.maximum(np.abs(h_analog), 1e-4))
    

    h_db_py = 20*np.log10(np.maximum(np.abs(h_py), 1e-4))
    
    # Grafico
    fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True)
    # MODULO
    fig.suptitle('ButterWorth N=2')
    ax.plot(w_py*nq/(np.pi*KHz), h_db_py,color='purple',linestyle='dashed', label = 'Digital')
    ax.plot(w_analog*fc/KHz, h_analog_db, color = 'orange',linestyle=':',  linewidth=3, label = 'Analogico')
    ax.grid(True)
    ax.set_title('Respuesta Magnitud $f_c = {} KHz$ | $f_s = {} KHz$'.format(fc/KHz, fs/KHz))
    ax.set_ylabel('Magnitud [dB]')
    ax.set_xlabel('Frecuencia [KHz]')
    ax.legend()
    ax.set_xlim([xlim1, xlim2])
    ax.set_ylim([ylim1, ylim2])
    
    
Q = np.sqrt(2)/2

# Pasa alto Butter
num = [1,  0,  0]
den = [1, 1/Q, 1]

fc = 6e3
fs = 100e3
TS8_funcion_c(fc, fs,num,den,0,50,-6,1)
#%% C).B Cambiamos la frecuencia de corte a 6KHz - fs = 10KHz
fc = 6e3
fs = 10e3
TS8_funcion_c(fc, fs,num,den,0,10,-12,1)


