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
import re

line = r'simdatabase/bulge_disk_f8/bdf8_73.fits	7318.831543	2195.564453	285.880737	1.500000	0.030000	23.756001	0.179520	27.990000	0.119100	jedisim_out/out0/stamp_0/stamp_0.fits.gz	jedisim_out/out0/distorted_0/distorted_0.fits'

regex1 = r'(.+?)(\d+)(\.w*)'
regex2 = r'(\w+?)(/distorted_)(\d+?)(\.w*)'
ngal = re.search(regex1,line).group(2)
nstamp = re.search(regex2,line).group(3)
print(ngal)
print(nstamp)
