#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics PhD. Student, Ohio University
# Date        : Feb 20, 2017
# Last update : May 09, 2017
# Est time    : 2 minutes 40 seconds
#
# Imports
from astropy.io import fits
import time


def fix_bad_headers(ingal, outgal):
    """Fix bad headers from original galaxies.

    Some of the files in original galaxies from
    web has byteordr problem.
    
    e.g. galaxy 1 has problem:
    BYTEORDR=           BIG_ENDIAN / SunOS, solaris etc. byte order 
    
    The value has no quotes around it.
    Same is true for galaxy0 and others.
    
    
    WARNING:
        This code fix_bad_byteordr.py will fail at galaxy202 from
        stamp_all/f814w_gal202.fits.
    
        So, first fix the tabbed keywords of this fitsfile using
        fix_bad_tabbed_headers.py
    
        Then run this code.

    """

    # read data and header from input fitsfiles
    hdul = fits.open(ingal)
    dat  = hdul[0].data
    hdr  = hdul[0].header
    
    # first delete bad header
    try:
        del hdr['BYTEORDR']
    except:
        pass
        
    # Then, write it again.
    hdr['BYTEORDR'] = 'BIG_ENDIAN'
    hdr['UPDATE']   = 'Edited headers by Bhishan Poudel on May 10, 2017'
    fits.writeto(outgal, dat, hdr, clobber=True)


def main():
    """Main program."""
    # ingal = /Users/poudel/jedisim/simdatabase/galaxies_original/f606w_gal0.fits
    pwd = '/Users/poudel/jedisim/simdatabase/'


    # update
    for i in range(0, 302):
        ingal  = pwd + 'stamps_all/f814w_gal' + str(i) + '.fits'
        outgal = pwd + 'galaxies/f814w_gal'   + str(i) + '.fits'
        print('galaxy:', i)
        fix_bad_headers(ingal, outgal)


if __name__ == '__main__':

    # beginning time
    program_begin_time = time.time()
    begin_ctime        = time.ctime()

    # run main program
    main()

    # print the time taken
    program_end_time  = time.time()
    end_ctime         = time.ctime()
    seconds           = program_end_time - program_begin_time
    m, s              = divmod(seconds, 60)
    h, m              = divmod(m, 60)
    d, h              = divmod(h, 24)
    print('\nBegin time: ', begin_ctime)
    print('End   time: '  , end_ctime, '\n')
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))
