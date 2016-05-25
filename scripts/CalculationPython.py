#!/usr/bin/env python3

import math
def GeneratePlot():
    pn = 1
    bn = 1
    hn = math.sqrt(pn**2 + bn ** 2)
    s = 0
    for i in range(10):               #iterate only 10 times
        An = 0.5 * pn * bn             # Area of nth trianlge
        bn = 0.5 * hn)                 
        pn = 1 - math.sqrt(1- bn ** 2)
        hn = math.sqrt(pn**2 + bn**2)
        s = s+( 2**i *An)
        res = 4*s
        print(res)
        
GeneratePlot()
