#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jan 4, 2017
# Last update :
# Est time    :

# Imports
import os
import subprocess
import glob
import re
import natsort


def missing_galaxies():
    """Missing galaxies.

    e.g. /Users/poudel/Research/galfit_usage/two_component_fit/galfit_outputs_0_301/devauc/f606w_devauc14.fits
    """
    galfit_outputs = 'galfit_outputs_0_301'
    pth = '/Users/poudel/Research/galfit_usage/two_component_fit/' +\
          galfit_outputs + '/devauc/f606w_devauc*.fits'
    nums = natsort.natsorted([int(re.search('(.+?)(\d+)(\.\w*)', f).group(2))
                              for f in glob.glob(pth)])
    missing = [i for i in list(range(0, 302)) if i not in nums]
    print('total number of missing galaxies: ', len(missing))
    print('missing galaxies: ', missing)

if __name__ == "__main__":
    missing_galaxies()
