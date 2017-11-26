import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
import scipy.constants as const
from uncertainties import ufloat
import math


def B(I):
    return I * (const.mu_0 / 2) * 195 * (0.109**2) / (0.109**2+(0.138/2)**2)**(3/2)
print("B0 bei 1A = ",B(1),"T")

Ik = (2/5)*0.1421*(0.0535/2)**2
print("Ikugel = ",Ik,"kg m^2")
