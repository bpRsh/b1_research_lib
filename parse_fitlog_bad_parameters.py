#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Feb 8, 2017


def parse_fitlog(fitlog):
    """Find bad parameters and write them into a file."""
    # imports
    import re
    import numpy as np

    # create empty file
    outfile = 'bad_paramters.csv'
    print('', file=open(outfile, 'w'))

    # initialize variables
    ingal = None
    expdisk = None
    nums = []

    # parse fit.log
    with open(fitlog, 'r') as f:
        # read all lines of fit.log
        for line in f:
            # get input galaxy name
            # */galaxies/f606w_gal0.fits[1:601,1:601]
            if line.strip().startswith("Input"):
                ingal = line[61:][0:-14]

            # expdisk paramters
            # expdisk   : (  295.40,   178.25)   19.21    437.65    0.87   -14
            # expdisk   : (  300.77,   300.94)  *78.29*    11.48    0.58   -79.46
            if line.strip().startswith("expdisk"):
                expdisk = line

                if '*' in line:
                    num = re.search('(.+?)(\d+)(\.fits)', ingal).group(2)
                    nums.append(num)
                    write = ingal + expdisk
                    print(ingal, line)
                    print(write, file=open(outfile, 'a'))
        # write all bad parameter galaxies in the end
        print(set(nums), file=open(outfile, 'a'))


if __name__ == "__main__":
    parse_fitlog('fit.log')
