#!/usr/bin/env python3


import math
from decimal import *

import numpy as np
import matplotlib.pyplot as plt

from matplotlib2tikz import save as tikz_save

def GeneratePlot():    
    getcontext().prec +=  21
    dec1 = Decimal(1); dec2 = Decimal(2); dec4 = Decimal(4); dec5 = Decimal(5); dec8 = Decimal(8); dec16 = Decimal(16)
    t = range(10)
    v = []
    decsum = Decimal(0)
    for i in t:
        deci = Decimal(i)
        cf = Decimal(dec1 / Decimal(16 ** i))
        td = dec4/(dec8 * deci + dec1) - dec2/(dec8 * deci + dec4) - dec1/(dec8 * deci +dec5) - dec1/(dec8 * deci + 6)
        tn = cf * td
        decsum = decsum + tn
        v.append(decsum)
        print(decsum)
        #print(4*s)
    plt.xlabel(r'Iterations $[n]$')
    plt.ylabel('Value of $\pi$ ')
    plt.grid(True)
    plt.plot(t,v,'o')
    #tikz_save('../Images/PIFastSeriesPlot.tex',figurewidth="12cm",figureheight="7cm")
    plt.show()

GeneratePlot();

