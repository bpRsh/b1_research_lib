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
    mynans    = []
    for i in range(1000):
        dat   = getdata('stamp_0/stamp_%d.fits.gz' % i)
        mysum = np.sum(dat)
        #print(mysum)
        if np.isnan(mysum):
            mynans.append(i)
            print('stamp_%d/stamp_%d.fits.gz ' % (i,k) , 'has sum = ', mysum)
            
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
        print('bad_gals = ', bad_gals)


