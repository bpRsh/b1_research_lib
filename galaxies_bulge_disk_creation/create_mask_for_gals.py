#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Jun 07, 2017 Wed
# Last update : 
#
#
# Imports
import time
import shutil
import os
import subprocess

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
def main():
    outfolder = 'masks'
    replace_outfolder(outfolder)
    
    for i in range(0,302):
        ifile = 'galaxies/f814w_gal%d.fits' % i
        ofile = '  > masks/f814w_mask%d.fits' % i
        cmd = "ic '0 1 %1 0 == ?'  " + ifile + ofile
        print('Creating: ', ofile)
        subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    main()
