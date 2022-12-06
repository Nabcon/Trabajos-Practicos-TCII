# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:11:10 2022

@author: Nahuel
"""

################### Punto 2) ############################

import scipy.signal as sig
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mediciones = 'TPL_mediciones.csv'
datos_mediciones = pd.read_csv(mediciones)

#INDEX
#f(KHz),|Vi|(V),|Vo|(mV),dT(useg)
freqs = datos_mediciones['f(KHz)'].to_numpy()*1000
T     = datos_mediciones['dT(useg)'].to_numpy()*1e-6

#########################################################


################### Punto 4) ############################

## PARTE SIMULACION
z,p,k = sig.cheb1ap(2, 1)
num_lp, den_lp = sig.zpk2tf(z,p,k)
num_hp, den_hp = sig.lp2hp(num_lp, den_lp)
sys = sig.TransferFunction(num_hp, den_hp)

f = np.logspace(-1, 2,10000)
w, mag, phase = sig.bode(sys,f)

fase_sim = np.zeros(15)

#normalizo valores medidos
"""
500  = 0.108696 -- index(w) = 120
1000 = 0.217391 -- index(w) = 1124
1100 = 0.239130 -- index(w) = 1262
1200 = 0.260870 -- index(w) = 1388
1300 = 0.282609 -- index(w) = 1504
2000 = 0.434783 -- index(w) = 2127
3000 = 0.652174 -- index(w) = 2714
4000 = 0.869565 -- index(w) = 3131
4600 = 1        -- index(w) = 3333
5000 = 1.086957 -- index(w) = 3454
6330 = 1.376087 -- index(w) = 3795
10k  = 2.173913 -- index(w) = 4457
20k  = 4.347826 -- index(w) = 5460
50k  = 10.86957 -- index(w) = 6787
100k = 21.73913 -- index(w) = 7790
"""
#busco el valor normalizado asociado al vector simulado y lo paso manualmente

fase_sim[0] = phase[120]
fase_sim[1] = phase[1124]
fase_sim[2] = phase[1262]
fase_sim[3] = phase[1388]
fase_sim[4] = phase[1504]
fase_sim[5] = phase[2127]
fase_sim[6] = phase[2714]
fase_sim[7] = phase[3131]
fase_sim[8] = phase[3333]
fase_sim[9] = phase[3454]
fase_sim[10] = phase[3795]
fase_sim[11] = phase[4457]
fase_sim[12] = phase[5460]
fase_sim[13] = phase[6787]
fase_sim[14] = phase[7790]

#############################################################

################### Punto 5) ################################

plt.plot(range(0,15),fase_sim,'o')

#############################################################




############### NO PONER EN EL JUPYTER PORQUE TIENE ERRORES######
# fase_aux   = np.zeros(16)
# fase_aux[0] = 180

# freqs_aux = np.zeros(16)
# for i in range(1,16):
#     freqs_aux[i] = freqs[i-1]

# freqs_aux[0]= 0
    
# for i in range(1,16):
#    fase_aux[i] = -T[i-1]*(freqs_aux[i]-freqs_aux[i-1]) + fase_aux[i-1] 

# plt.plot(range(15),V_out)
#############################################################
