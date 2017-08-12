#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Tue Mar 21, 2017
# Last update :
# Est time    : 1 minute 11 sec

# Imports
from astropy.io import fits
import time


def add_headers():
    """Add headers to a fitsfile."""
    
    count = 2


    galaxy   = '/Users/poudel/jedisim/simdatabase/galaxies'
    ingal    = galaxy + '/f814w' + '_gal' + str(count) + '.fits'

    # headers for output files
    MAG      = float(fits.getval(ingal, 'MAG'))
    RADIUS   = float(fits.getval(ingal, 'RADIUS'))
    MAG0     = float(fits.getval(ingal, 'MAG0'))
    PIXSCALE = 0.03
    if count >= 101:
        PIXSCALE = 0.06

    #  Note:
    #  MAG0 = 30       for 0-100
    #  MAG0 = 26.6611  for f606w band 101-301
    #  MAG0 = 26.78212 for f814w band 101-301

    # input and output dir
    indir   = '/Users/poudel/jedisim/simdatabase/bulge_f8_missing_headers/'
    outdir  = '/Users/poudel/jedisim/simdatabase/bulge_f8/'
    infile  = indir + 'f814w_bulge'  + str(count) + '.fits'
    outfile = outdir + 'f814w_bulge' + str(count) + '.fits'

    dat, hdr        = fits.getdata(infile, ext=0, header=True)
    hdr['BYTEORDR'] = 'BIG_ENDIAN'
    hdr['MAG']      = MAG
    hdr['MAG0']     = MAG0
    hdr['PIXSCALE'] = PIXSCALE
    hdr['RADIUS']   = RADIUS
    
    # write and print
    fits.writeto(outfile, dat, hdr, clobber=True)
    print("\n\ningal:", infile)
    print("outgal   :", outfile)


if __name__ == "__main__":
    # beginning time
    program_begin_time = time.time()
    begin_ctime = time.ctime()

    #  Run the main program
    add_headers()

    # print the time taken
    program_end_time = time.time()
    end_ctime = time.ctime()
    seconds = program_end_time - program_begin_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print("nBegin time: ", begin_ctime)
    print("End   time: ", end_ctime, "\n")
    print("Time taken: {0: .0f} days, {1: .0f} hours, \
    {2: .0f} minutes, {3: f} seconds.".format(d, h, m, s))
