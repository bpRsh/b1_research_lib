#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jan 4, 2017
# Update      : Jun 19, 2017 Mon


# Imports
from astropy.io.fits import getval
import numpy as np
import pandas as pd
from pandas import DataFrame as DF

# Pandas setting
pd.set_option('display.width', None)
pd.set_option('precision', 3)

# Variables
NCOLS = 7
f606  = '/Users/poudel/jedisim/z_jedisim_dev_sim/stamps_f6/f606w_gal'
f814  = '/Users/poudel/jedisim/z_jedisim_dev_sim/galaxies/f814w_gal'
OFILE = 'mag_diff_f6_f8.txt'

def mag_diff_f6_f8(f606, f814,ngals):
    """Find difference in magnitudes of f606 and f814 bands."""
    diff =  [   getval(f606 + str(n) + '.fits', 'MAG') 
             - getval(f814 + str(n) + '.fits', 'MAG')   
                   for n in range(ngals) 
            ]
            
    return [ round(x,2) for x in diff]
    

def write_mag_diff():
    print('Writing: ', OFILE)
    # Create data frames
    # Note: 7*43 = 301
    lst1, lst2 = np.arange(301), mag_diff_f6_f8(f606, f814,301)
    arr1, arr2 = np.array_split(lst1, NCOLS), np.array_split(lst2, NCOLS)
    df1, df2  = DF(arr1).T, DF(arr2).T

    # Assign column names
    clm = [ 'Galaxy_%d'%i for i in range(NCOLS)]
    df1.columns, df2.columns = clm, clm

    # Combine respective columns and create new df.
    for i in range(7):
        df1.insert(i*2+1,'Diff_%d'%i,df2['Galaxy_%d'%i])

    # Print and write df
    df1.columns = [ 'Galaxy', 'Diff']*7
    df1.to_csv(OFILE,float_format='%.3f',sep='\t',index=None)
    #print(df1)

def write_mag_diff2():
    diff  = mag_diff_f6_f8(f606, f814,302)
    ofile = 'mag_diff_one_col.txt'
    print('Writing: ', ofile)
    with open(ofile,'w') as fo:
        for i in range(302):
            line = str(i) + '  ' + str(diff[i]) + '\n'
            fo.write(line)
    

if __name__ == '__main__':
    write_mag_diff()
    write_mag_diff2()
