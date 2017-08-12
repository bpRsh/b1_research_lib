#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Feb 9, 2017
# Last update :
# Est time    :

# Imports
from astropy.io import fits
import numpy as np


def find_centroid(fitsfile):
    """Find centroid of the fitsfile."""
    dat = fits.getdata(fitsfile)
    indices = np.where(dat == dat.max())
    y1, x1 = list(zip(indices[0], indices[1]))[0]  # first maximum value of matrix
    y1, x1 = y1 + 1, x1 + 1
    max1 = [x1, y1]

    # to find second max, make maximum value zero and repeat above process
    dat[indices] = 0.0
    indices = np.where(dat == dat.max())
    y2, x2 = list(zip(indices[0], indices[1]))[0]  # first maximum value of matrix
    y2, x2 = y2 + 1, x2 + 1
    max2 = [x2, y2]

    # find physical center of image
    x0, y0 = np.matrix(dat).shape

    # get distances of maxima from center
    dx = [x1 - x0, x2 - x0]
    nearest = min(max1, max2)
    print(nearest)
    # print(np.max(dat))
    # print(x, y)
    return (max1, max2)


if __name__ == "__main__":
    x, y = find_centroid('/Users/poudel/jedisim/simdatabase/galaxies/f606w_gal145.fits')
    print(x, y)
