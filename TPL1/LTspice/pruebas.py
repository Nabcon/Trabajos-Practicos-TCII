# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 01:07:56 2022

@author: Nahuel
"""


import math as m
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

alfa_max = 1

ee = 10**(alfa_max/10)-1
e = m.sqrt(ee)
w0 = 1

num=[0.892, 0, 0]
den=[1, 0.996*w0, 0.907*w0**2]

sys = sig.TransferFunction(num, den)
f = np.logspace(-1, 1,1000)
w, mag, phase = sig.bode(sys,f)

fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
ax1.semilogx(w,mag,label='|T(w)|')
ax1.grid(True)
ax1.set_title('Magnitude Response')
ax1.set_ylabel('Magnitude[dB]')
ax1.legend()

ax2.semilogx(w, phase,color='red',label='ang[T(w)]')
ax2.grid(True)
ax2.set_title('Phase Response')
ax2.set_ylabel('Phase[deg]')
ax2.legend()