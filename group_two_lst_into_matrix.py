#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jun 16, 2017 Fri
# Last update : 
#
# Imports
import numpy as np
import pandas as pd
import time
import pprint

a  = np.arange(302)
a2 = 2 * a
b  = np.array_split(a, 302//20+1)
b2 = np.array_split(a2, 302//20+1)

with open('tmp.txt','w') as fo:
    for i in range(len(b2)):
        bl    = [str(_) for _ in b[i]]
        b2l   = [str(_) for _ in b2[i]]
        bstr  = str(i) + ':  ' +  " ".join(bl) + '\n'
        b2str = str(i) + ':  ' + " ".join(b2l) + '\n\n'
        fo.write(bstr)
        fo.write(b2str)


