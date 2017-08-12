#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Nov 21, 2016
# Last update :
# Est time    :

# Imports
import os
import glob
import re

# renaming fitsfiles
files = glob.glob('bulge_f8/*.fits')
for file in files:
    try:
        os.rename(file, file.replace('_gal', '_bulge'))
    except:
        pass

# renaming fitsfiles
files = glob.glob('disk_f8/*.fits')
for file in files:
    try:
        os.rename(file, file.replace('_gal', '_disk'))
    except:
        pass
