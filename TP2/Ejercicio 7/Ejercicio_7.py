# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 23:11:18 2022

@author: Nahuel
"""

import math as m
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

f_0  = 2e3
f_s1 = 1.25e3
f_s2 = 3.2e3
f_p1 = 1.6e3
f_p2 = 2.5e3
alfa_min = 20
alfa_max = 3

Q = f_0/(f_p2-f_p1)

ee = 10**(alfa_max/10)-1
e = m.sqrt(ee)

n = 3

p_bp = [1, 1/Q, (2*Q**2+1)/Q**2, 1/Q, 1]

raices_bp = np.roots(p_bp)
r1_bp = [raices_bp[0], raices_bp[1]]
r2_bp = [raices_bp[2], raices_bp[3]]

#Encuentro los coeficientes del polinomio asociado a esos pares de polos
p1_bp = np.poly(r1_bp)
p2_bp = np.poly(r2_bp)

num = [10**0.5/Q**3, 0, 0, 0]
den = np.convolve([1, 1/Q, 1], p_bp)

sys = sig.TransferFunction(num, den)
f = np.logspace(-0.5, 0.5,1000)
w, mag, phase = sig.bode(sys,f)
fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
ax1.semilogx(w,mag,label='|T(w)|')
ax1.grid(True)
ax1.set_title('Modulo de Transferencia')
ax1.set_yticks([-40,-30,-20,-10,0,7,10])
ax1.set_ylabel('Magnitude[dB]')
ax1.legend()

ax2.semilogx(w, phase,color='red',label='ang[T(w)]')
ax2.grid(True)
ax2.set_title('Phase Response')
ax2.set_ylabel('Phase[deg]')
ax2.set_xticks([0.625,0.8,1,1.25,1.6])
ax2.set_xticklabels(['$\omega_{S1}$','$\omega_{P1}$','$\omega_0$','$\omega_{P2}$','$\omega_{S1}$'])
ax2.legend()




