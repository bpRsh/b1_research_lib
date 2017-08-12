#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jan 4, 2017
# Update      : Jun 07, 2017 Wed
# 
# Imports
import os
import subprocess
import glob
import re
import natsort
from astropy.io.fits import getdata
import numpy as np


def find_nan_in_fits():
    """Check if a fitsfile has nan values in it."""
    # get nan values
    mynans = []
    for i in range(0,12):
        for j in range(0,1000):
            k = i*1000+j
            dat = getdata('stamp_%d/stamp_%d.fits.gz' % (i,k))
            mysum = np.sum(dat)
            if np.isnan(mysum):
                mynans.append(k)
                print('stamp_%d/stamp_%d.fits.gz ' % (i,k) , 'has sum = ', mysum)
                
    # stamp_12 has 12420 stamps

    for j in range(12000,12420):
        #print(12, j)
        dat = getdata('stamp_12/stamp_%d.fits.gz' % j)
        mysum = np.sum(dat)
        if np.isnan(mysum):
            mynans.append(j)
            
    return mynans


if __name__ == "__main__":
    mynans     = find_nan_in_fits()
    bad_stamps = ['stamp_%d.fits.gz' %i for i in mynans]
    bad_gals   = []
    regex1     = r'(.+?)(\d+)(\.w*)'
    regex2     = r'(\w+?)(/distorted_)(\d+?)(\.w*)'
    
    # Write nan stamps to a new file
    with open('trial1_catalog.txt', 'r') as fi,\
         open('nan_stamps.txt', 'w') as fo:
             
        for line in fi.readlines():
            for bs in bad_stamps:
                if bs in line:
                    badgal   = re.search(regex1,line).group(2)
                    badstamp = re.search(regex2,line).group(3)                  
                    bad_gals.append(badgal)
                    new_line = 'bdf8_%s.fits stamp_%s.fits.gz\n' % (badgal, badstamp)
                    fo.writelines(new_line)
            
        bad_gals = list(set(bad_gals))
        bad_gals = natsort.natsorted(bad_gals)
        print("\n")
        print('bad_gals      = ', bad_gals)
        print('len bad_gals  = ', len(bad_gals)  )
        print('len good_gals = ', 302 - len(bad_gals))

