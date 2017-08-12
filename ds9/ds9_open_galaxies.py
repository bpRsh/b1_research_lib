#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jan 4, 2017
#
# Imports
import os
import subprocess
import glob
import re
import natsort
from astropy.io.fits import getval


def open_in_ds9():
    """Open fitsfiles in ds9 with some flgs."""
    # ds9 commands
    ds9 = '/Applications/ds9.app/Contents/MacOS/ds9' + ' '
    
    files = [ 'bulge_disk_f8/bdf8_%d.fits' %i for i in range(302)]
    filenames = ' '.join(files)
    
    cmd = ds9 + ' -height 1200 ' + ' -width 2500 ' +  filenames
    print(cmd[0:100])
    subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    open_in_ds9()
