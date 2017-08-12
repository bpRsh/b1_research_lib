#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Feb 11, 2017
# Last update :
# Est time    :

# Imports
import pandas as pd
import numpy as np

infile = 'ssp_pf.cat'

# read sixth column (6 Gyr)
# First column is wavelength
# Second column is 1 Gyr old star flux
b6 = np.genfromtxt(infile, delimiter=None, usecols=(6), dtype=float)
print(b6[:4])


# using pandas
infile   = infile
colnames = ['c0', 'c5']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(0,5))

print(df.head())
print("\n")
