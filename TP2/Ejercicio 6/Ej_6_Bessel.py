# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 18:50:57 2022

@author: Nahuel
"""
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import splane as tc2

num = [105]
den = [1, 10, 45, 105, 105]

z,p,k = sig.cheb1ap(3, 1)
num_lp, den_lp = sig.zpk2tf(z,p,k)

r_t = np.roots(den)
r2 = [p[0], p[2]]
r1 = [p[1]]

coeficientes = np.poly(p)

p1 = np.poly(r1)
p2 = np.poly(r2)

# sos_pbanda = tc2.tf2sos_analog(num, den)
# tc2.analyze_sys( sos_pbanda )