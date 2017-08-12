#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jan 4, 2017
# NOTE: While viewing in ds9, set scale of first galaxy to minmax
# then, match scale and limits.
# I could not find ds9 flags to do that.

# Imports
import os
import subprocess
import glob
import re
import natsort
from astropy.io.fits import getval


def open_in_ds9(n, galfit_outputs):
    """Open fitsfiles in ds9 with some flgs.

    Arguments:     n: galaxy number

    ds9 flgs:
        ds9 -scale log -cmap a -match cmap -match scalelimits FITSFILES_NAMES

    ds9 interface:
        Scale > log
        Color > a
        Frame > Match > Colorbar
        Scale > Scale Parameters > -0.05 to 0.05
        Frame > Match > Scale and limits

    Reference:
        http://ds9.si.edu/doc/ref/command.html#scale

    """
    # path of four fitsfiles to open
    gal = '~/jedisim/simdatabase/'
    fit = '~/Research/galfit_usage/two_component_fit/' + galfit_outputs + '/'
    flgs = '-scale log -cmap a -tile grid layout 10 4' + ' ' +\
        '-match colorbar -match scale -match scalelimits' + ' '

    pth = '/Users/poudel/Research/galfit_usage/two_component_fit/' +\
          galfit_outputs + '/bulge/f606w_bulge*.fits'
    nums = natsort.natsorted([int(re.search('(.+?)(\d+)(\.\w*)', f).group(2))
                              for f in glob.glob(pth)])
    # print(nums)

    files_lst = [
        fit + 'bulge/f606w_bulge' + str(n + m) + '.fits ' + flgs +
        fit + 'disk_only/f606w_disk' + str(n + m) + '.fits ' + flgs +
        fit + 'residual/f606w_res' + str(n + m) + '.fits ' + flgs +
        fit + 'disk_res/f606w_disk' + str(n + m) + '.fits ' + flgs +
        gal + 'galaxies/f606w_gal' + str(n + m) + '.fits ' + flgs
        for m in range(8) if (n + m) in nums]
    files = " ".join(files_lst)

    # flgs for ds9
    # files = files1 + files2 + files3 + files4 + files5 + files6 + files7 +\
    #     files8
    ds9 = '/Applications/ds9.app/Contents/MacOS/ds9' + ' '
    cmd = ds9 + ' -height 1200 ' + ' -width 2500 ' + files
    subprocess.call(cmd, shell=True)


def find_color(f606, f814):
    """Find difference in magnitudes of f606 and f814 bands."""
    mag1 = getval(f606, 'MAG')
    mag2 = getval(f814, 'MAG')

    # print(f606[-20:], '   :mag606 - mag814 =', mag1 - mag2)
    print(f606[-20:], '==>', '%.2f' % (mag1 - mag2))


def main():
    """Run main function."""
    galfit_outputs = 'galfit_outputs_0_301'
    pth = '/Users/poudel/Research/galfit_usage/two_component_fit/' +\
          galfit_outputs + '/bulge/f606w_bulge*.fits'
    nums = natsort.natsorted([int(re.search('(.+?)(\d+)(\.\w*)', f).group(2))
                              for f in glob.glob(pth)])
    # choose your range of galaxies
    nums = [x for x in nums if (x > 194 and x < 200)]
    print('nums: ', nums)
    missing = [i for i in list(range(0, 301)) if i not in nums]
    print('missing:', missing)
    # /Users/poudel/jedisim/simdatabase/galaxies/f606w_gal195.fits
    f606 = '/Users/poudel/jedisim/simdatabase/galaxies/f606w_gal'
    f814 = '/Users/poudel/jedisim/simdatabase/galaxies/f814w_gal'

    # print magnitude difference
    for n in nums:
        find_color(f606 + str(n) + '.fits', f814 + str(n) + '.fits')
    # display 8 or less galaxies in the list nums, and their fittings in ds9
    for i, n in enumerate(nums[::8]):
        print('Galaxy number: ', n)
        open_in_ds9(n, galfit_outputs)


if __name__ == "__main__":
    main()
