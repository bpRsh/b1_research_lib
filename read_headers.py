#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Feb 10, 2017
# Last update :
# Est time    :

# Imports
import numpy as np
from astropy.io import fits
import glob
import re


f = '/Users/poudel/jedisim/simdatabase/galaxies/f606w_gal101.fits'

pix = fits.getval(f, 'PIXSCALE')
ltv1 = fits.getval(f, 'LTV1')
ltv2 = fits.getval(f, 'LTV2')
flux = fits.getval(f, 'FLUX')
mag = fits.getval(f, 'MAG')
radius = fits.getval(f, 'RADIUS')
mag0 = fits.getval(f, 'MAG0')

# print(num, pix)
print(pix, ltv1, ltv2, flux, mag, radius, mag0)
