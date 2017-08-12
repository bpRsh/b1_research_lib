#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Jun 07, 2017 Wed
# Last update : 
#
# Estimated time: 1 min 36 sec for bulge only
# Imports
import subprocess
import os
import time
import astropy.io
from astropy.io import fits

def replace_outfolder(outfolder):
    """Replace given directory."""
    # imports
    import shutil
    import os

    if os.path.exists(outfolder):
        print('Replacing folder: ', outfolder)
        shutil.rmtree(outfolder)
        os.makedirs(outfolder)
    else:
        print('Making new folder: ', outfolder)
        os.makedirs(outfolder)

def multiply_two_fits(ifits1, ifits2, ofits):
    """Multiply two fits files."""
    # data
    dat1, hdr1 = fits.getdata(ifits1, header=True)
    dat2, hdr2 = fits.getdata(ifits2, header=True)
    dat_out = dat1 * dat2

    #print(dat1[301][280:300])
    #print(dat2[301][280:300])
    #print(dat_out[301][280:300])
    fits.writeto(ofits, dat_out, hdr1, clobber=True)

    print('{} {} {}'.format('Output file: ', ofits, ''))

def mask_bulge():
    outfolder = 'bulge_f8'
    replace_outfolder(outfolder)
    
    for i in range(0,302):
        ifits1 = 'bulge_f8_unmasked/f814w_bulge_unmasked%d.fits' % i
        ifits2 = 'masks/f814w_mask%d.fits' % i
        ofits  = 'bulge_f8/f814w_bulge%d.fits' % i
        multiply_two_fits(ifits1, ifits2, ofits)

def mask_disk():
    outfolder = 'disk_f8'
    replace_outfolder(outfolder)
    
    for i in range(0,302):
        ifits1 = 'disk_f8_unmasked/f814w_disk_unmasked%d.fits' % i
        ifits2 = 'masks/f814w_mask%d.fits' % i
        ofits  = 'disk_f8/f814w_disk%d.fits' % i
        multiply_two_fits(ifits1, ifits2, ofits)

##==============================================================================
## Main program
##==============================================================================
if __name__ == '__main__':

    # Beginning time
    begin_time,begin_ctime = time.time(), time.ctime()

    # Run main program
    mask_bulge()
    #mask_expdisk_res()

    # Print the time taken
    end_time,end_ctime     = time.time(), time.ctime()
    seconds                = end_time - begin_time
    m, s                   = divmod(seconds, 60)
    h, m                   = divmod(m, 60)
    d, h                   = divmod(h, 24)
    print('\nBegin time: ', begin_ctime,'\nEnd   time: ', end_ctime,'\n' )
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

