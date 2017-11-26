import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
import scipy.constants as const
from uncertainties import ufloat
import math

m = 0.0014
Ik = (2/5)*0.1421*(0.0535/2)**2

def B(I):
    return I * (const.mu_0 / 2) * 195 * (0.109**2) / (0.109**2+(0.138/2)**2)**(3/2)

r, I = np.genfromtxt('content/values/gravitation_val.txt', unpack=True)

r /= 1000
B = B(I)

def f(x, b):
    return x*b

parameters, pcov = curve_fit(f, r, B)
errors = np.sqrt(np.diag(pcov))

a = ufloat(parameters[0], errors[0])
print('Steigung a = {0:.8f}'.format(a),'T/m')

t= np.linspace(r[0],r[len(r)-1],5000)
plt.plot(t, f(t, *parameters), 'k-', label='Regression')
plt.plot(r, B, 'kx', label='Messwerte')
plt.xlabel(r'$r/[m]$')
plt.ylabel(r'$B(I)/ [T]$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/gravitation.pdf')
print('Der Dipolmoment beträgt: ',m*const.g/a,'Am^2')
print('--------------------------------')
