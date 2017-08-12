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

bad_gals =  [ '7', '9', '12', '15', '26', '34', '35', '39', '42', '50', '55', 
'61', '62', '64', '65', '66', '72', '77', '78', '94', '96', '99', '101', '102', 
'108', '111', '112', '113', '116', '127', '140', '142', '147', '149', '151', 
'156', '157', '162', '163', '165', '167', '170', '173', '174', '178', '179', 
'186', '188', '189', '190', '193', '195', '196', '197', '204', '205', '206', 
'212', '213', '215', '222', '224', '228', '232', '237', '242', '245', '246', 
'249', '260', '262', '268', '271', '272', '276', '277', '286', '287', '296', 
'297', '298', '300', '301']



print('len of bad_gals_for_stamp0 = ', len(bad_gals)) # 83

def open_in_ds9():
    """Open fitsfiles in ds9 with some flgs."""
    # ds9 commands
    ds9 = '/Applications/ds9.app/Contents/MacOS/ds9' + ' '
    
    files = [ 'bulge_disk_f8/bdf8_%s.fits' %i for i in bad_gals ]
    filenames = ' '.join(files)
    
    cmd = ds9 + ' -height 1200 ' + ' -width 2500 ' +  filenames
    print(cmd)
    subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    open_in_ds9()
