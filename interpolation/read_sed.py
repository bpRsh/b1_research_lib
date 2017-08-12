#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : May 31, 2017
# Last update : 
#
#
# Imports
import time
import numpy as np

# input file
infile = 'ssp_pf.cat'


# Method 1
# empty lists
col0, col6, col12 = [], [], []
with open(infile,'r') as inf:
    for line in inf:
        if not line.startswith('#'):
            parts = line.split()  # split line into parts
            if len(parts) > 1:    # if at least 2 parts/columns
                col0.append(parts[0])
                col6.append(parts[6])
                col12.append(parts[12])

print(col0[0:5])
#print(col6[0:5])
#print(col12[0:5])


# Method 2
col0, col6, col12 = np.loadtxt(infile, skiprows=15, unpack=True,
                               dtype='float', usecols=(0, 6, 12))

print(col0[0:5])
#print(col6[0:5])
#print(col12[0:5])
