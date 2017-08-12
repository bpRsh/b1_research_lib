#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Feb 20, 2017
# Last update : May 10, 2017 Wed
# Est time    : 10 sec for f814w 302 galaxies

# Imports
from astropy.io import fits
import time


def read_headers_galaxies():
    pwd = '/Users/poudel/jedisim/simdatabase/'   
    for i in range(302):
        
        # Reading headers of bulge f814 galaxies
        ingal = pwd + 'bulge_f8/f814w_bulge'  + str(i) + '.fits'
        
        
        # Get headers
        mag   = fits.getheader(ingal)['MAG']
        mag0  = fits.getheader(ingal)['MAG0']
        rad   = fits.getheader(ingal)['RADIUS']
        pix   = fits.getheader(ingal)['PIXSCALE']

        
        ## For bulge
        print('f814w_bulge', i,   ':', 'MAG = ', mag, 'MAG0 = ', mag0,
              'RADIUS = ', rad, 'PIXSCALE = ', pix)


def read_headers_bluge_f8():
    pwd = '/Users/poudel/jedisim/simdatabase/'   
    for i in range(302):
        
        # Reading headers of bulge f814 galaxies
        ingal = pwd + 'bulge_f8/f814w_bulge'  + str(i) + '.fits'
        
        
        # Get headers
        mag   = fits.getheader(ingal)['MAG']
        mag0  = fits.getheader(ingal)['MAG0']
        rad   = fits.getheader(ingal)['RADIUS']
        pix   = fits.getheader(ingal)['PIXSCALE']

        
        ## For bulge
        print('f814w_bulge', i,   ':', 'MAG = ', mag, 'MAG0 = ', mag0,
              'RADIUS = ', rad, 'PIXSCALE = ', pix)

def read_headers_disk_f8():
    pwd = '/Users/poudel/jedisim/simdatabase/'   
    for i in range(302):
        
        # Reading headers of bulge f814 galaxies
        ingal = pwd + 'disk_f8/f814w_disk'  + str(i) + '.fits'
        
        
        # Get headers
        mag   = fits.getheader(ingal)['MAG']
        mag0  = fits.getheader(ingal)['MAG0']
        rad   = fits.getheader(ingal)['RADIUS']
        pix   = fits.getheader(ingal)['PIXSCALE']

        
        ## For disk
        print('f814w_disk', i,   ':', 'MAG = ', mag, 'MAG0 = ', mag0,
              'RADIUS = ', rad, 'PIXSCALE = ', pix)
        

if __name__ == '__main__':

    # beginning time
    program_begin_time = time.time()
    begin_ctime = time.ctime()

    # run main program
    read_headers_galaxies()
    #read_headers_bluge_f8()
    #read_headers_disk_f8()

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
