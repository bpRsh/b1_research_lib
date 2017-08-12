#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Feb 22, 2017
# Imports
import re
import numpy as np
import os


def create_log_table(fitlog, outfile):
    """Make a data table from fit.log."""
    # parse fit.log
    with open(fitlog, 'r') as f, \
            open(outfile, 'w') as fo:
        for line in f:
            # get input galaxy name
            # Input image     : simdatabase/galaxies/f814w_gal0.fits[1:601,]
            if line.strip().startswith("Input"):
                l = line.strip()
                pattern = '(.+?)(f814.+?)(\.fits*)'
                gal = re.search(pattern, l).group(2) + '.fits'
                # print(gal)

            # expdisk paramters
            # expdisk   : (  295.40,   178.25)   19.21    437.65    0.87   -14
            # expdisk   : (  300.77,   300.94)  *78.29*    11.48    0.58   -79.46
            num_list = []
            if line.strip().startswith("expdisk"):
                expdisk = line
                good = 1
                if '*' in expdisk:
                    good = 0
                num_list = list(map(float, re.findall(r"""(?:-)?   # negative
                                               \d+                 # digits
                                               (?:\.\d+)?          # decimal
                                               """, expdisk, re.X)))  # VERBOSE
                print(gal, num_list[0], num_list[1], num_list[2], num_list[3],
                      num_list[4], num_list[5], good, file=fo)


if __name__ == "__main__":
    fitlog = '/Users/poudel/Research/galfit_usage/expdisk_devauc_fitting_parameter_fixed/fit_expdisk_f8_feb13.log'
    outfile = 'log_table_expdish_f8.csv'
    create_log_table(fitlog, outfile)
