# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:37:48 2022

@author: Nahuel
"""

import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt


nn = 5 # orden
alfa_max = 0.5 # dB
ee = 10**(alfa_max/10)-1
e = np.sqrt(ee)

# Mediante las funciones de python obtengo la transeferncia cheby n=5
z,p,k = sig.cheb1ap(nn, alfa_max)
num_lp, den_lp = sig.zpk2tf(z,p,k)

#### MANUAL ####

# expando el binomio del polinomio de chebyshev n=5
a1 = np.array([16, 0, -20, 0, 5, 0.0])
a2 = np.array([16, 0, -20, 0, 5, 0.0])
aux1 = np.convolve(a1,a2)

# reemplazo a las W por S/J, me quedan negativos los coeficientes
aux1[0] *= -1
aux1[4] *= -1
aux1[8] *= -1

# agrego el termino independiente
aux1[10] = 1/ee

#obtengo las raices de de T(S) y T(-S)
aux2 = np.roots(aux1)

# me quedo solo con las raices de T(S)
raices_totales = [aux2[2], aux2[3], aux2[6], aux2[7], aux2[8]]

r1 = [raices_totales[0], raices_totales[1]]
r2 = [raices_totales[2], raices_totales[3]]
r3 = [raices_totales[4]]

p1 = np.poly(r1)
p2 = np.poly(r2)
p3 = np.poly(r3)

# obtengo los coeficientes asociados a las raices seleccionadas
den = np.poly(raices_totales)

# escribo el numerador
num = [0, 0, 0, 0, 0, 1/(e*16)]


###compropbacion manuial
c1 = [1, 0.236, 1.05]
c2 = [1, 0.622, 0.493] 
c3 = np.convolve(c1,c2)
den_c = np.convolve(c3,[1,0.385])


sys = sig.TransferFunction(num, den_c) #calculado
sys2 = sig.TransferFunction(num_lp, den_lp) #transferencia por python

# vector de frencuencia logaritmado
f = np.logspace(-2, 2,10000)

# obtengo la magnitud y fase de las transferencias
w, mag, phase = sig.bode(sys,f)
w2, mag2, phase2 = sig.bode(sys2,f)

fig, (ax1,ax2) = plt.subplots(nrows=2 , ncols=1, sharex=True)
# MODULO
ax1.semilogx(w,mag,label='calculado')
ax1.semilogx(w2,mag2,color='red',linestyle='dashed',label='python')
ax1.grid(True)
ax1.set_title('Magnitude Response')
ax1.set_ylabel('Magnitude[dB]')
ax1.legend()

# FASE
ax2.semilogx(w, phase,color='purple',label='calculado')
ax2.semilogx(w2,phase2,color='orange',linestyle='dashed',label='python')
ax2.grid(True)
ax2.set_title('Phase Response')
ax2.set_ylabel('Phase[deg]')
ax2.legend()
