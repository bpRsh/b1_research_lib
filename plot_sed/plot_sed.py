#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jun 24, 2016
# Last update : May 31, 2017
   
# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# input/output
infile   = 'ssp_pf.cat'
outimage = 'bulge6' + '.png'

# read in a file
infile   = infile
colnames = ['c0', 'c5']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(0,5))

print(df.head())
print("\n")


## plot wavelength vs flux
fig, ax = plt.subplots()
plt.plot(df.c0,df.c5,linewidth=1,color='b')

# title and axes labels
plt.title(infile)
plt.xlabel(r'Wavelength ($\AA$) ', fontsize=14)
plt.ylabel(r'Flux', fontsize=14)



# axes limit
#plt.xlim(500,700)
#plt.ylim(1e-12,7e-12)

# grid and margins
plt.grid(True)
fig.subplots_adjust(left=0.2) 
fig.subplots_adjust(bottom=0.2) 

# print
outimage = outimage
print('{} {}'.format('\noutput image = ',outimage ))
plt.savefig(outimage)
plt.show()
