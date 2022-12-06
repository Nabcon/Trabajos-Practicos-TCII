# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 04:20:36 2022

@author: Nahuel
"""

import math as m
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import splane as tc2


f_s = 12e3
f_p = 40e3
w_ns = f_s/f_p
w_np = f_p/f_p
Omega_s = 1/w_ns
Omega_p = 1/w_np

alfa_max = 1

ee = 10**(alfa_max/10)-1
e = np.sqrt(ee)

nn = 4

z,p,k = sig.cheb1ap(nn, alfa_max)

r1_lp = [p[0], p[3]]
r2_lp = [p[1], p[2]]

p1_lp = np.poly(r1_lp)
p2_lp = np.poly(r2_lp)

const = 1/(8*e)
num = [const]
A = ee*64
p_lp = [1, 0, 2, 0, 1.25, 0, 0.25, 0, (ee+1)/A]

x=1.01368*3.57912*const

raices_lp = np.roots(p_lp)
rt_lp = [raices_lp[0], raices_lp[1], raices_lp[4], raices_lp[5]]
poly_lp = np.poly(rt_lp)

pol_1pr = [1, 0.2829, 1.01368]


pol_2pr = [1, 2.4114, 3.5719]
num_pr = [x, 0, 0, 0, 0]
pol_hpr = np.convolve(pol_1pr,pol_2pr)

sys = sig.TransferFunction(num_pr, pol_hpr)
f = np.logspace(-2, 2,10000)
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

ans =  1.01368*3.5719*const
z,p,k = sig.cheb1ap(nn, alfa_max)
num_lp, den_lp = sig.zpk2tf(z,p,k)
num_bp, den_bp = sig.lp2hp(num_lp, den_lp)


# w0 = 1

# num=[0.892, 0, 0]
# den=[1, 0.996*w0, 0.907*w0**2]
# sys = sig.TransferFunction(num, den)
# sos_pbanda = tc2.tf2sos_analog(num, den)
# tc2.analyze_sys( sos_pbanda )