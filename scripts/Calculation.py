#!/usr/bin/env python3


import math
from decimal import *

import numpy as np
import matplotlib.pyplot as plt

from matplotlib2tikz import save as tikz_save

def GeneratePlot():    
    getcontext().prec +=  2
    pn = Decimal(1)
    bn = Decimal(1)
    hn = Decimal(math.sqrt(pn**2 + bn ** 2))
    f = Decimal(0.5)
    g = Decimal(1)
    s = 0
    t = range(10)
    v = []
    for i in t:
        An = Decimal(f * pn * bn)
        bn = Decimal(f * hn)
        pn = Decimal(g - Decimal(math.sqrt(g- bn ** 2)))
        hn = Decimal(math.sqrt(pn**2 + bn**2))
        s = Decimal(s+( 2**i *An))
        res = 4*s
        v.append(res)
        print(res)
    plt.xlabel(r'Iterations $[n]$')
    plt.ylabel('Value of $\pi$ ')
    plt.grid(True)
    plt.plot(t,v,'o')
    tikz_save('../Images/PISeriesPlot.tex',figurewidth="12cm",figureheight="7cm")

GeneratePlot();

