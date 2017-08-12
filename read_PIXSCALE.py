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

for i in range(0, 301):
    f = '/Users/poudel/jedisim/simdatabase/galaxies/f814w_gal' + str(i) + '.fits'
    f = '/Users/poudel/jedisim/simdatabase/galaxies/f606w_gal' + str(i) + '.fits'
    num = re.search("(.+?)(\d+)(\.\w*)", f).group(2)
    pix = fits.getval(f, 'PIXSCALE')
    mag0 = fits.getval(f, 'MAG0')
    # print(num, pix)
    print(num, mag0)
