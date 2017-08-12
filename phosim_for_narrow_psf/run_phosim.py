#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 12, 2016
# Last update : 
#
# Inputs      : instance_catalog : examples/star         
#               background       : examples/nobackground
#               output_folder    : output
#
# Outputs     : output/output_todays_date_time/17_zipped_psf_fitsfiles
#               we need only electron image lsst_e_***.fits.gz.
#
# Info:
# 1. This program runs phosim software.
#    basic command of phosim is go to directory of phosim.py:
#    ./phosim instance_catalog -c physics_command -o outputdir
#
#  Estimated time : 4 minutes for magnitude = 20 and nobackground
#  Estimated time : 3 minutes for examples/star and nobackground
#
#  NOTE: run program in the external terminal


# Imports
import subprocess
import os   
import time
import shutil

# Global variables
outputdir1 = 'output/output' + time.strftime("_%b_%d_%H_%M/")

def replace_outdir(outdir):
    """Replace a folder."""    
    if os.path.exists(outdir):
        print('Replacing folder: %s\n'%outdir)
        shutil.rmtree(outdir)
        os.makedirs(outdir)
    else:
        print('Making new folder: %s\n'%outdir)
        os.makedirs(outdir)

def run_phosim():
    """Run the phosim program to get psf (electron image) 
    for a given instance catalog and background."""
    
    # Commands to run
    instance_catalog  = '/Users/poudel/phosim/examples/star'
    background        = '/Users/poudel/phosim/examples/nobackground'
    outputdir2        = '/Users/poudel/tmp/' + outputdir1
    commands = 'cd ~/phosim;' + \
               ' ./phosim '   + instance_catalog + \
               ' -c '         + background + \
               ' -o '         + outputdir2

    # Input/output info
    print('{} {} {}'.format('outputdir        = ',outputdir1, ''))       
    print('{} {} {}'.format('instance_catalog = ',instance_catalog, '\n\n'))       
          
    # Run the phosim to get electron images.
    subprocess.call(commands,shell=True)

def main():
    replace_outdir(outputdir1)
    run_phosim()
    
   
if __name__ == '__main__':
    # Beginning time
    begin_time,begin_ctime = time.time(), time.ctime()

    # Run main program
    main()

    # Print the time taken
    end_time,end_ctime  = time.time(), time.ctime()
    seconds             = end_time - begin_time
    m, s                = divmod(seconds, 60)
    h, m                = divmod(m, 60)
    d, h                = divmod(h, 24)
    print('\nBegin time: ', begin_ctime,'\nEnd   time: ', end_ctime,'\n' )
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

## NOTE: run program in the external terminal
