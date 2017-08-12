#!/usr/bin/env python3
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

# renaming f606 files
files = glob.glob('bulge/*.fits')
for file in files:
    try:
        os.rename(file, file.replace('_gal', '_bulge'))
    except:
        pass
