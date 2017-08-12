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
import pandas as pd

infile = 'ssp_pf_interpolated.csv' 
columns = ['wav','age6','age12']
df = pd.read_csv(infile, sep=r'\s+',names=columns)

df2 = df.loc[0:10, :]
print(df2)


# example 2
newdf = df[(df['wav']>1002) & (df['wav']<1008)]
print(newdf)
