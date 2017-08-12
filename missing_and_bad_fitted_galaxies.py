#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jan 4, 2017
# Last update : Feb 12, 2017
# Est time    :

# Imports
import os
import subprocess
import glob
import re
import natsort


def missing_galaxies(pth, num_gals):
    """Missing galaxies.

    e.g. /Users/poudel/Research/galfit_usage/expdisk_devauc_fitting/galfit_outputs/residual/f606w_res0.fits
    """
    nums = natsort.natsorted([int(re.search('(.+?)(\d+)(\.\w*)', f).group(2))
                              for f in glob.glob(pth)])
    missing = [i for i in list(range(0, num_gals)) if i not in nums]
    return missing, len(missing)


def parse_fitlog(fitlog):
    """Find bad parameters and write them into a file."""
    # imports
    import re
    import numpy as np
    from natsort import natsorted

    # initialize variables
    ingal = None
    expdisk = None
    nums = []

    # parse fit.log
    with open(fitlog, 'r') as f:
        # read all lines of fit.log
        for line in f:
            # get input galaxy name
            # # */galaxies/f606w_gal0.fits[1:601,1:601]
            if line.strip().startswith("Input"):
                ingal = line[61:][0:-15]

            if '*' in line:
                bad = line
                num = re.search('(.+?)(\d+)(\.\w*)', ingal).group(2)
                nums.append(num)
                write = ingal + bad

        # list of  bad fitted galaxies
        bad = list(map(int, set(nums)))
        bad = natsort.natsorted(bad)

        # two groups
        bad100 = [i for i in bad if i <= 100]
        bad200 = [i for i in bad if i >= 101]
    return bad, bad100, bad200


def main(pth, log):
    # missing
    total = 302
    missing, nmissing = missing_galaxies(pth, total)
    missing100 = [i for i in missing if i <= 100]
    missing200 = [i for i in missing if i >= 101]
    nmissing100 = len(missing100)
    nmissing200 = len(missing200)

    # summary of missing galaxies
    print('missing100     = ', missing100)
    print('nmissing100    = ', nmissing100)
    print('missing200     = ', missing200)
    print('nmissing200    = ', nmissing200)

    # bad parameters
    bad, bad100, bad200 = parse_fitlog(log)
    nbad, nbad100, nbad200 = len(bad), len(bad100), len(bad200)

    # summary of bad fitted galaxies
    print('nbad     = ', nbad)
    print('nbad100  = ', nbad100)
    print('nbad200  = ', nbad200)
    print('bad     = ', bad)
    print('bad100  = ', bad100)
    print('bad200  = ', bad200)

    # total summary
    nmissing300 = nmissing100 + nmissing200
    nbad300     = nbad100 + nbad200
    nmissing_bad300 = nmissing300 + nbad300
    ngood300 = total - nmissing_bad300
    print('total           = ', total)
    print('nmissing300     = ', nmissing300)
    print('nbad300         = ', nbad300)
    print('nmissing_bad300 = ', nmissing_bad300)
    print('ngood300        = ', ngood300)


if __name__ == "__main__":
    pwd = '/Users/poudel/Research/galfit_usage/expdisk_devauc_fitting/'
    pth = pwd + 'galfit_outputs_f8/residual/f8*.fits'
    log = pwd + 'fit_f8_all_corrected_feb12.log'
    main(pth, log)
