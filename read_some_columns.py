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

infile = 'centroidsf8.csv'

# read first 2 columns
df = pd.read_csv(infile, sep=' ', skipinitialspace=True, header=None)
df2 = df.loc[:, [0, 1]]
# df2.to_csv(infile, header=None, index=None, sep=' ')
print(df2.head())


# usecols
df2 = pd.read_csv(infile, sep='\s+', skipinitialspace=True, header=None,
                  usecols=[0, 1])
print(df2.head())

# numpy.genfromtxt and np.savetxt
data = np.genfromtxt(infile, delimiter=None, usecols=(0, 1), dtype=int)
print(data[:4])
np.savetxt('temp.csv', data, fmt='%.0f', delimiter=' ')
