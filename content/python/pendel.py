import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
import scipy.constants as const
from uncertainties import ufloat
import math

Ik = (2/5)*0.1421*(0.0535/2)**2

def B(I):
    return I * (const.mu_0 / 2) * 195 * (0.109**2) / (0.109**2+(0.138/2)**2)**(3/2)

I, T = np.genfromtxt('content/values/pendel_val.txt', unpack=True)

T /= 10 # Eine Periodendauer
B = B(I)

y = T**2
x = 1/B


def f(x, b):
    return x*b

parameters, pcov = curve_fit(f, x, y)
errors = np.sqrt(np.diag(pcov))

a = ufloat(parameters[0], errors[0])
print('Steigung a = {0:.8f}'.format(a),'Ts^2')

t= np.linspace(x[0],x[len(x)-1],5000)
plt.plot(t, f(t, *parameters), 'k-', label='Regression')
plt.plot(x, y, 'kx', label='Messwerte')
plt.xlabel(r'$[T]/B$')
plt.ylabel(r'$T^2/ [s^2]$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/pendel.pdf')
print('Der Dipolmoment beträgt: ',4*(const.pi**2)*Ik/a,'Am^2')
print('--------------------------------')
