#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Feb 20, 2017
# Last update :
# Est time    : 2 minutes

# Imports
from __future__ import division, unicode_literals, print_function
from astropy.io import fits
import time


def multiply_fitsfile(ingal, outgal):
    """Multiply input fitsfile by 24000.

    This program converts the pixel values from COUNT/SEC to COUNT
    chosen EXPTIME = 40 minutes = 40 * 60 = 2400 sec

    Note: while doing this conversion I encountered problems for two fitsfiles:
    /Users/poudel/jedisim/simdatabase/galaxies_original/f606w_gal284.fits
    /Users/poudel/jedisim/simdatabase/galaxies_original/f814w_gal202.fits

    The first one had bad values for keyword MAG.
    The second one had bad keywords FLUX\t, MAG\t, RADIUS\t.

    Script to fix these errors are:
    /Users/poudel/jedisim/simdatabase/fix_bad_values_or_keywords_of_fitsfile/fix_bad_MAG.py
    /Users/poudel/jedisim/simdatabase/fix_bad_values_or_keywords_of_fitsfile/fix_bad_tabbed_keyword_FLUX_RADIUS.py

    NOTE: The fitsfiles also have BYTEORDR problem, I have also fixed them.
    NOTE: I have also added some comments.

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
    hdr['UPDATE'] = 'Multiplied original datavalues by 2400'
    hdr['UPDATEBY'] = 'Edited by Bhishan Poudel, Feb 20 2017'
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
        print('galaxy f606w : ', i)
        multiply_fitsfile(ingal, outgal)

    # f814w band
    for i in range(0, 302):
        ingal = pwd + 'galaxies_original/f814w_gal' + str(i) + '.fits'
        outgal = pwd + 'galaxies/f814w_gal' + str(i) + '.fits'
        print('galaxy f814w : ', i)
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
