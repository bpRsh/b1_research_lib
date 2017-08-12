#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-19-2016 Wed
# Last update :
#
#
# Imports
from astropy.io import fits
import numpy as np

dat1 = np.arange(0, 20).reshape(4, 5)
dat1[2, 1] = 50.0  # x,y = 2, 3 (numpy inverts x and y and starts from zero)
hdu = fits.PrimaryHDU(dat1)
hdu.writeto('new.fits', clobber=True)


# >>> numpy.matrix('1 2; 3 4')
# >>> numpy.arange(25).reshape((5, 5))
# >>> numpy.array(range(25)).reshape((5, 5))
# >>> numpy.ndarray((5, 5))
