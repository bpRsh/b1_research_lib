#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : 26-Oct-2016 13:10
# Last update : Dec 15, 2016
# Est time    : 3 min for one galaxy one filter.
# Main commands : rm -r imgblock.fits subcomps.fit ; galfit expdisk_devauc.sh
#                 galfit -o3 galfit.01 && rm -r galfit.01
#                 ds9 -multiframe imgblock.fits subcomps.fits &

# Imports
from __future__ import division, unicode_literals, print_function
from astropy.io import fits
import time


def multiply_fitsfile(ingal, outgal):
    """Multiply input fitsfile by 24000.

    We are changing count/pixels to counts.
    exposure time = 2400 sec.
    """

    # read data and header from input fitsfiles
    hdul = fits.open(ingal)
    dat = hdul[0].data
    hdr = hdul[0].header
    try:
        del hdr['BYTEORDR']
    except:
        pass

    hdr['BYTEORDR'] = 'BIG_ENDIAN'
    new_dat = dat * 2400
    fits.writeto(outgal, new_dat, hdr, clobber=True)

    # # check
    # print('old pixel value 301 301 = ', dat[301][301])
    # print('new pixel value 301 301 = ', new_dat[301][301])


def main():
    """Main program."""
    # example
    # ingal = /Users/poudel/jedisim/simdatabase/galaxies_original/f606w_gal0.fits
    pwd = '/Users/poudel/jedisim/simdatabase/'

    # f606w band
    for i in range(0, 302):
        ingal = pwd + 'galaxies_original/f606w_gal' + str(i) + '.fits'
        outgal = pwd + 'galaxies/f606w_gal' + str(i) + '.fits'
        print('galaxy:', i)
        multiply_fitsfile(ingal, outgal)

    # f814w band
    for i in range(0, 302):
        ingal = pwd + 'galaxies_original/f814w_gal' + str(i) + '.fits'
        outgal = pwd + 'galaxies/f814w_gal' + str(i) + '.fits'
        print('galaxy:', i)
        multiply_fitsfile(ingal, outgal)


if __name__ == '__main__':

    # beginning time
    program_begin_time = time.time()
    begin_ctime = time.ctime()

    # run main program
    main()

    # print the time taken
    program_end_time = time.time()
    end_ctime = time.ctime()
    seconds = program_end_time - program_begin_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print('\nBegin time: ', begin_ctime)
    print('End   time: ', end_ctime, '\n')
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))
