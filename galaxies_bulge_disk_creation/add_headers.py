#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Tue Mar 21, 2017
# Last update :
#
# Est time    : 3 minute 20 sec for 302 bulge and disk files.
# Imports
from astropy.io import fits
import time


def add_headers_to_bulge():
    """Add headers to bulge.
    
    From: bulge_f8_missing_headers
    To  : bulge_f8_unmasked
    
    """

    num_source_images = 302
    for count in range(0, num_source_images):
        
        # Original input galaxies
        ingal    = 'galaxies/f814w_gal%d.fits' % count

        # Read headers from original galaxies
        MAG      = float(fits.getval(ingal, 'MAG'))
        RADIUS   = float(fits.getval(ingal, 'RADIUS'))
        MAG0     = float(fits.getval(ingal, 'MAG0'))
        PIXSCALE = float(fits.getval(ingal, 'PIXSCALE'))

        # Read also some other headers
        LTV1     = float(fits.getval(ingal, 'LTV1'))
        LTV2     = float(fits.getval(ingal, 'LTV2'))
        FLUX     = float(fits.getval(ingal, 'FLUX'))

        # Input/output
        infile  = 'bulge_f8_missing_headers/f814w_bulge%d.fits' % count
        outfile = 'bulge_f8_unmasked/f814w_bulge_unmasked%d.fits' % count

        dat, hdr        = fits.getdata(infile, ext=0, header=True)
        hdr['MAG']      = MAG
        hdr['MAG0']     = MAG0
        hdr['PIXSCALE'] = PIXSCALE
        hdr['RADIUS']   = RADIUS
        hdr['LTV1']     = LTV1
        hdr['LTV2']     = LTV2
        hdr['FLUX']     = FLUX
        hdr['BYTEORDR'] = 'BIG_ENDIAN'
        hdr['UPDATE']   = 'Added headers MAG MAG0 RADIUS BYTEORDR LTV1 LTV2 FLUX by Bhishan Poudel on date June 7, 2017'
        
        # Write and print
        fits.writeto(outfile, dat, hdr, clobber=True)
        print("\n\n")
        print("ingal  :", infile)
        print("outgal :", outfile)

def add_headers_to_disk():
    """Add headers to disk.
    
    From: disk_f8_missing_headers
    To  : disk_f8_unmasked
    
    """

    num_source_images = 302
    for count in range(0, num_source_images):
        
        # original input galaxies from web
        ingal    = 'galaxies/f814w_gal%d.fits' % count

        # Read headers from original galaxies from web
        MAG      = float(fits.getval(ingal, 'MAG'))
        RADIUS   = float(fits.getval(ingal, 'RADIUS'))
        MAG0     = float(fits.getval(ingal, 'MAG0'))
        PIXSCALE = float(fits.getval(ingal, 'PIXSCALE'))

        # Read also some other headers
        LTV1     = float(fits.getval(ingal, 'LTV1'))
        LTV2     = float(fits.getval(ingal, 'LTV2'))
        FLUX     = float(fits.getval(ingal, 'FLUX'))

        # /Users/poudel/jedisim/simdatabase/disk_f8_missing_headers/f814_disk0.fits
        infile  = 'disk_f8_missing_headers/f814w_disk%d.fits' % count
        outfile = 'disk_f8_unmasked/f814w_disk_unmasked%d.fits' % count

        dat, hdr        = fits.getdata(infile, ext=0, header=True)
        hdr['MAG']      = MAG
        hdr['MAG0']     = MAG0
        hdr['PIXSCALE'] = PIXSCALE
        hdr['RADIUS']   = RADIUS
        hdr['LTV1']     = LTV1
        hdr['LTV2']     = LTV2
        hdr['FLUX']     = FLUX
        hdr['BYTEORDR'] = 'BIG_ENDIAN'
        hdr['UPDATE']   = 'Added headers MAG MAG0 RADIUS BYTEORDR LTV1 LTV2 FLUX by Bhishan Poudel on date June 7, 2017'
        
        # write and print
        fits.writeto(outfile, dat, hdr, clobber=True)
        print("\n\n")
        print("ingal  :", infile)
        print("outgal :", outfile)


if __name__ == "__main__":
    # beginning time
    program_begin_time = time.time()
    begin_ctime = time.ctime()

    #  Run the main program
    #add_headers_to_bulge()
    add_headers_to_disk()

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
