# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:32:34 2022

@author: Nahuel
"""

import math as m


w_p1 = 1.6e6
w_p2 = 2.5e6
w_s1 = 1.25e6
w_s2 = 3.2e6

w0 = m.sqrt(w_p1 * w_p2)

w0_n = 1
w_p1_n = w_p1 / w0
w_p2_n = w_p2 / w0
w_s1_n = w_s1 / w0
w_s2_n = w_s2 / w0

BW_n = w_p2_n - w_p1_n

Q = w0_n / BW_n
Omega_s2 = Q * (w_s2_n ** 2 - 1) / w_s2_n

alpha_max = 3
alpha_min = 20
Omega_s = Omega_s2

# butterworth -- alpha_max = 3
epsilon = m.sqrt(10 ** (alpha_max/10) - 1)
N_B = m.log10((10 ** (alpha_min/10) - 1) / (10 ** (alpha_max/10) - 1)) / 2 / m.log10(Omega_s)

# chebyshev
N_C = m.acosh(m.sqrt((10**(alpha_min/10)-1)/(10**(alpha_max/10)-1)))/m.acosh(13/6)




