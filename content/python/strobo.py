import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
import math

Ik = (2/5)*0.1421*(0.0535/2)**2
nu = 4.5 #Hertz

def B(I):
    return I * (const.mu_0 / 2) * 195 * (0.109**2) / (0.109**2+(0.138/2)**2)**(3/2)

I, T1, T2, T3 = np.genfromtxt('content/values/strobo_val.txt', unpack=True)

T = (T1+T2+T3)/3

B = B(I)

y = 1/T
x = B

def f(x, b):
    return x*b

parameters1, pcov1 = curve_fit(f, x, 1/T1)
errors1 = np.sqrt(np.diag(pcov1))
a1 = ufloat(parameters1[0], errors1[0])
parameters2, pcov2 = curve_fit(f, x, 1/T2)
errors2 = np.sqrt(np.diag(pcov2))
a2 = ufloat(parameters2[0], errors2[0])
parameters3, pcov3 = curve_fit(f, x, 1/T3)
errors3 = np.sqrt(np.diag(pcov3))
a3 = ufloat(parameters3[0], errors3[0])

print(a1,a2,a3)
parameters, pcov = curve_fit(f, x, y)
errors = np.sqrt(np.diag(pcov))

a = np.mean([a1,a2,a3])
print('Steigung a = {0:.8f}'.format(a),'Ts^2')

t= np.linspace(x[0],x[len(x)-1],5000)
plt.plot(t, f(t, *parameters), 'k-', label='Regression')
plt.plot(x, y, 'kx', label='Messwerte')
plt.xlabel(r'$[T]/B$')
plt.ylabel(r'$T^2/ [s^2]$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/strobo.pdf')
print('Der Dipolmoment beträgt: ',4*(const.pi**2)*Ik*nu*a,'Am^2')
print('---------------------------------')
