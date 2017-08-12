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


def find_nan_in_fits(infile):
    """Check if a fitsfile has nan values in it."""
    # get nan values
    print('Reading: ', infile)
    dat = getdata(infile)
    mysum = np.sum(dat)
    if np.isnan(mysum):
        print(infile , 'has sum = ', mysum)
            
    #return mynans

def main():
    for f in glob.glob('bulge_f8/f814w_bulge*.fits'):
        find_nan_in_fits(f)
    
    for f in glob.glob('disk_f8/*.fits'):
        find_nan_in_fits(f)
    
    for f in glob.glob('bulge_disk_f8/*.fits'):
        find_nan_in_fits(f)



if __name__ == "__main__":
    main()


