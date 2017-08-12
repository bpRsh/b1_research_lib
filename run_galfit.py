#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : 26-Oct-2016 13:10
# Last update :
# Est time    :

# Imports

from __future__ import division, unicode_literals, print_function
import subprocess
import os
import time
from string import ascii_uppercase
import astropy.io
from astropy.io import fits
from astropy.io.fits import getdata
from astropy.io.fits import getheader
from astropy.io.fits import getval

paramfile = r'sim2.feedme'


def replace_galfit_param(name, value, object_num=1, fixed=True):
    """Replace input galfit parameter file with new configuration.

    Arguments:

    name : parameter name, e.g. A-P,  1-10, 'Z'
    value: new value for the parameter in string form. e.g. '20.0'
    object_num: For A-Z object_num is 1
                For objects, object_num starts from 1.
    fixed: True means parameter will be fixed during fitting.
    """
    name, value = str(name), str(value)
    with open(paramfile) as f:
        gf_file = f.readlines()

    # Location of param.
    loc = [i for i in range(len(gf_file)) if
           gf_file[i].strip().startswith(name + ')')][object_num - 1]
    param_str = gf_file[loc]
    comment = param_str.find('#')
    if name in ascii_uppercase:
        fmt = '{}) {} {}'
        param_str = fmt.format(name, value, param_str[comment:])
    else:
        fmt = '{}) {} {}         {}'
        param_str = fmt.format(name, value, '0' if fixed else '1',
                               param_str[comment:])
    gf_file[loc] = param_str
    with open(paramfile, 'w') as f:
        f.writelines(gf_file)


def find_centroid(fitsfile):
    """Find centroid of the fitsfile."""
    dat = fits.getdata(fitsfile)
    print(np.max(dat))

    indices = np.where(dat == dat.max())
    y, x = list(zip(indices[0], indices[1]))[0]  # first maximum value of matrix
    y, x = y + 1, x + 1
    # print(x, y)
    return (x, y)


def run_galfit(galaxy, outdir, count):
    """Run galfit on the input galaxy and create model and residual images.

    Runs galfit on the given input galaxies and creates model
        and residue images in the output directory

        galaxy : base name of input galaxy, e.g f606w or f814w
        outdir : output directory, e.g. galfit_outputs
        count  : count number of galaxy, e.g. 0 for f606w_gal0.fits

        Needs  : galfit_outputs/two_components/bulge/
                 galfit_outputs/two_components/disk/
                 galfit_outputs/two_components/residual/

        Note: 1. This program will also read the values of mag and rad from the
              input fitsfile header, and updates the value in the
              galfit paramfile 'sim2.feedme'.

              2. it will also create the mask file using ic command.

    """
    # galaxy = f606w or f814w
    path = '/Users/poudel/jedisim/simdatabase/colors'
    ingal = path + '/' + galaxy + '_gal' + str(count) + '.fits'
    psf = galaxy + '_psf.fits'  # psf in the same directory

    #  get the value of magnitude and radius of input galaxy
    mag = getval(ingal, 'MAG')
    rad = getval(ingal, 'RADIUS')

    # create galfit paramfile according to the input galaxy
    # For A-Z object_num is 1
    # fixed=True means it is fixed and not changed
    print('{} {} {}'.format('\n\nGalaxy =  ', ingal, '\n\n'))
    replace_galfit_param('A', ingal, object_num=1, fixed=False)
    replace_galfit_param('D', psf, object_num=1, fixed=False)

    # create mask file according to the input galaxy
    cmd = "ic '1 0 %1 0 == ?'  " + ingal + "  > mask.fits"
    subprocess.call(cmd, shell=True)

    # For objects, object_num starts from 1
    # 1 = expdisk, 2 = devauc
    for obj_num in [1, 2]:
        replace_galfit_param('3', mag, object_num=obj_num, fixed=False)
        replace_galfit_param('4', rad, object_num=obj_num, fixed=False)

        # run galfit
        # rm -r imgblock.fits subcomps.fits galfit.01 # removes these files.
        # galfit sim.feedme  # gives galfit.01, imgblock.fits,if succeed.
        # galfit -o3 galfit.01  # runs only when galfit.01 exists
        # we can delete galfit.01 immediately after it it used.
        cmd1 = 'rm -r imgblock.fits; galfit ' + paramfile
        cmd2 = 'rm -r subcomps.fits; galfit -o3 galfit.01; rm -r galfit.01'
        print("\n\n\n")
        print('*' * 60)
        print('Running: {}'.format(cmd1))
        print('*' * 60)
        subprocess.call(cmd1, shell=True)  # gives galfit.01 if succeed

        if os.path.exists('galfit.01'):

            print("\n\n\n")
            print('*' * 60)
            print('Running: {}'.format(cmd2))
            print('*' * 60)
            subprocess.call(cmd2, shell=True)

    # get residual map from imgblock.fits
    residual = outdir + '/residual/' + galaxy + '_res' + str(count) + '.fits'

    # get devauc and expdisk models from subcomps.fits
    # galaxy = f606w or f814w
    # devauc = bulge and expdisk+residual = disk
    devauc = outdir + '/bulge/' + galaxy + '_bulge' + str(count) + '.fits'
    expdisk_res = outdir + '/disk/' + galaxy + '_disk' +\
        str(count) + '.fits'

    # extracting frames of imgblock.fits and subcomps.fits if they exists.
    if os.path.isfile('subcomps.fits') and os.path.isfile('imgblock.fits'):

        # for imgblock.fits : 0 is empty, 1 is input, 2 is model, 3 is residual
        dat_res, hdr_res = fits.getdata(r'imgblock.fits', ext=3, header=True)

        # for subcomps.fits: 0 is input, 1 is expdisk, 2 is devauc etc.
        dat_exp, hdr_exp = fits.getdata(r'subcomps.fits', ext=1, header=True)
        dat_dev, hdr_dev = fits.getdata(r'subcomps.fits', ext=2, header=True)

        #  fits.writeto(expdisk, dat_exp, hdr_exp, clobber=False)
        fits.writeto(residual, dat_res, hdr_res, clobber=False)
        fits.writeto(devauc, dat_dev, hdr_dev, clobber=False)
        fits.writeto(expdisk_res, dat_exp + dat_res, hdr_exp, clobber=False)

        # print('{} {} {}'.format('Output file: ', expdisk, ''))
        print('{} {} {}'.format('Output file: ', residual, ''))
        print('{} {} {}'.format('Output file: ', devauc, ''))
        print('{} {} {}'.format('Output file: ', expdisk_res, ''))


def main():
    """Main program."""
    # output directory without '/' in the end
    # range is from 0 to 101 and both f606w and f814w
    galfit_outdir = 'galfit_outputs'

    #  for count in list(range(0, 101)):
    for count in list(range(0, 1)):

        run_galfit('f606w', galfit_outdir, count)
        run_galfit('f814w', galfit_outdir, count)


if __name__ == '__main__':

    # beginning time
    program_begin_time = time.time()
    begin_ctime = time.ctime()

    # run main program
    main()

    # print the time taken
    program_end_time = time.time()
    end_ctime = time.ctime()
    seconds = program_end_time - program_begin_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print('\nBegin time: ', begin_ctime)
    print('End   time: ', end_ctime, '\n')
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))
