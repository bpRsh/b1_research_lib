#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jan 19, 2017
# Last update :
# cmd    : ds9 f814w_devauc_res0.fits mask.fits multiplied.fits

# Imports
from __future__ import division, unicode_literals, print_function
import subprocess
import os
import time
import astropy.io
from astropy.io import fits



def multiply_two_fits(fits1, fits2, out):
    """Multiply two fits files."""
    # data
    dat1, hdr1 = fits.getdata(fits1, header=True)
    dat2, hdr2 = fits.getdata(fits2, header=True)
    dat_out = dat1 * dat2

    print(dat1[301][280:300])
    print(dat2[301][280:300])
    print(dat_out[301][280:300])
    fits.writeto(out, dat_out, hdr1, clobber=True)

    print('{} {} {}'.format('Output file: ', out, ''))

if __name__ == '__main__':
    fits1 = 'f814w_devauc_res0.fits'
    fits2 = 'mask.fits'
    out = 'multiplied.fits'
    multiply_two_fits(fits1, fits2, out)

    # open in ds9
    ds9 = '/Applications/ds9.app/Contents/MacOS/ds9' + ' '
    files = 'f814w_devauc_res0.fits mask.fits multiplied.fits'
    cmd = ds9 + files
    subprocess.call(cmd, shell=1)
