#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jan 4, 2017
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
    dat = getdata('trial1_HST.fits')
    mysum = np.sum(dat)
    print('mysum = ', mysum)
    
    # max
    mymax = -1e16
    print('Finding maximum ...')
    for i in range(len(dat)):
        m = max(dat[i])
        
        if m > mymax:
            mymax = m
    print('max = ', mymax)
    
    # min
    mymin = 1e16
    print("\n")
    print('Finding minimum ...')
    for i in range(len(dat)):
        m = min(dat[i])
        
        if m < mymin:
            mymin = m
    print('min = ', mymin)
        
if __name__ == "__main__":
    find_nan_in_fits()
