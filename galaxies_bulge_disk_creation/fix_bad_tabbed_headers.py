#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : 26-Oct-2016 13:10
# Last update : May 10, 2017 Wed
# Imports
from astropy.io import fits
import time


def modify_fitsfile(ingal, outgal):
    """Modify bad magnitude value.

    i = 202  # f814w_gal202.fits gives bad keyword error.

    # from ds9 I see that
    FLUX	= 7.1217
    MAG  	= 24.6507
    RADIUS	= 4.010
    
    I could not find problem from ds9 headers.
    
    I have to correct it manually.
    First get the values from ds9 and rep
    
    I had moved f814w_gal202.fits from stamp_f8 folders to 
    stamp_bad and will write the new corrected fitsfile inside
    stamp_all.
    
    Then, I will run fix_bad_byteordr.py again.
    """

    # read data from input fitsfiles
    hdul            = fits.open(ingal)
    dat             = hdul[0].data
    
    # read header from good input galaxy
    good = '/Users/poudel/jedisim/simdatabase/stamps_f8/f814w_gal201.fits'
    hdr             = fits.getheader(good)
    
    # Now, update this header by correct values
    hdr['FLUX']     = 7.1217
    hdr['MAG']      = 24.6507
    hdr['RADIUS']   = 4.010
    hdr['PIXSCALE'] = 0.06
    hdr['MAG0']     = 26.78212
    hdr['LTV1']     = 283.0
    hdr['LTV2']     = 276.0
    hdr['BYTEORDR'] = 'BIG_ENDIAN'
    hdr['HISTORY']  = 'Edited by Bhishan Poudel, Ohio University'

    # write corrected fitsfile
    fits.writeto(outgal, dat, hdr, clobber=True)


def main():
    """Main program."""
    # example
    # ingal = '/Users/poudel/jedisim/simdatabase/stamps_all/f814w_gal202.fits'
    pwd    = '/Users/poudel/jedisim/simdatabase/'
    ingal  = pwd + 'stamps_bad/f814w_gal202.fits'
    outgal = pwd + 'stamps_f8/f814w_gal202.fits'
    print('writing: ', outgal)

    modify_fitsfile(ingal, outgal)


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
