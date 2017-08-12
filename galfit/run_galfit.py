#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : 26-Oct-2016 13:10
# Last update : Feb 12, 2017
# Est time    : 3 min for one galaxy one filter.
# Main commands : rm -r imgblock.fits subcomps.fit ; galfit expdisk_devauc.sh
#                 galfit -o3 galfit.01 && rm -r galfit.01
#                 ds9 -multiframe imgblock.fits subcomps.fits &

# Imports
from string import ascii_uppercase
from astropy.io import fits
import numpy as np
import subprocess
import time
import os


paramfile = r'expdisk_devauc.sh'


def replace_galfit_param(name, value, object_num=1, fixed=True):
    """Replace input galfit parameter file with new configuration.

    Arguments:

    name : parameter name, e.g. A-P,  1-10, 'Z'
    value: new value for the parameter in string form. e.g. '20.0'
    object_num: For A-Z object_num is 1
                For objects, object_num starts from 1.
    fixed: True means parameter will be fixed (0) during fitting.

    NOTE: Keep fixed = False while using this function to vary the parameter.
    """
    name, value = str(name), str(value)
    with open(paramfile) as f:
        gf_file = f.readlines()

    # Location of param.
    # 3rd column is where one can hold the parameters fixed (0) or allow vary 1
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


def run_galfit(galaxy, outdir, count, centroid_file):
    """Run galfit on the input galaxy and create model and residual images.

    Runs galfit on the given input galaxies and creates model
        and residue images in the output directory

        galaxy        : base name of input galaxy, e.g f606w or f814w
        outdir        : output directory, e.g. galfit_outputs
        count         : count number of galaxy, e.g. 0 for f606w_gal0.fits
        cetnroid_file : input file having centoids of 302 galaxies for given
                        band, e.g.
                        centroidsf6.csv, centroidsf8.csv
                        created by: find_centroid.py

        Needs  :
        input galaxy  : /Users/poudel/jedisim/simdatabase/galaxies/f606w_gal0.fits
                        /Users/poudel/jedisim/simdatabase/galaxies/f814w_gal0.fits
        output dir    : galfit_outputs/devauc
                        galfit_outputs/devauc_res
                        galfit_outputs/expdisk
                        galfit_outputs/expdisk_res
                        galfit_outputs/residual
        psf            : f606w_psf.fits
                         f606w_psf.fits
                         psf are created using TinyTim website
        mask           : mask.fits
                         ic '1 0 %1 0 == ?'  INPUT_GALAXY  > mask.fits
        paramfile      : expdisk_devauc.sh
                         input parameter file for galfit
                         (example from tar file of GALFIT website)
        centroid file  : a data file containing x,y position of input galaxy
                         it is created by centoid.py
                         right now, I have chosen the brightest pixel co-ordinate
                         to be the centroid of the galaxy. It may not be true
                         for some galaxies, but in most of the cases when it is
                         not true galfit fails whether I update centoid or not.

        Features:
        1. Following parameters on input paramfile for galfit are updated
           a) input galaxy name
           b) psf for that galaxy
           c) mask is created using ic command
           d) mag0,pixscale,mag,radius using astropy.fits.getval
           e) position or centroid using input file created from centroid.py
        2. Temporary files created in each loop
           a) mask.fits using ic '1 0 %1 0 == ?'  INPUT_GALAXY  > mask.fits
           b) imgblock.fits (0 is empty, 1 is input, 2 is model, 3 is residual)
           c) subcomps.fits (0 is input, 1 is expdisk, 2 is devauc etc.)

    """
    # galaxy = f606w or f814w
    path = '/Users/poudel/jedisim/simdatabase/galaxies'
    ingal = path + '/' + galaxy + '_gal' + str(count) + '.fits'
    psf = galaxy + '_psf.fits'  # psf in the script directory

    #  get the value of magnitude, radius and mag0 of input galaxy
    try:
        mag = fits.getval(ingal, 'MAG')
    except:
        mag = 20.0

    # read radius
    try:
        rad = fits.getval(ingal, 'RADIUS')
    except:
        rad = 10.0

    # get mag0
    #  MAG0 = 30       for 0-100
    #  MAG0 = 26.6611  for f606w band 101-301
    #  MAG0 = 26.78212 for f814w band 101-301
    try:
        mag0 = fits.getval(ingal, 'MAG0')
    except:
        pass

    # save time: instead reading fitsfile just use the if statement!
    # 0-100, including, has PIXSCALE = 0.03  and rest has 0.06
    PIXSCALE = '0.03 0.03'
    if count >= 101:
        PIXSCALE = '0.06 0.06'

    # find centroid of the input galaxy
    infile = centroid_file
    _, x, y = np.loadtxt(infile, unpack=True)
    centroid = str(x[count]) + ' ' + str(y[count]) + ' 1'

    # create galfit paramfile according to the input galaxy
    # For A-Z object_num is 1
    # fixed=True means it is fixed and not changed
    print("\n\n\n")
    print('+' * 80)
    print('+' * 80)
    print('+' * 80)
    print('{} {} {}'.format('Current Galaxy :  ', ingal, ''))
    print('+' * 80)
    print('+' * 80)
    print('+' * 80)

    # update control paramters
    replace_galfit_param('A', ingal, object_num=1, fixed=False)
    replace_galfit_param('D', psf, object_num=1, fixed=False)
    replace_galfit_param('J', mag0, object_num=1, fixed=False)
    replace_galfit_param('K', PIXSCALE, object_num=1, fixed=False)

    # object 1 is expdisk
    replace_galfit_param('1', centroid, object_num=1, fixed=False)
    replace_galfit_param('3', mag, object_num=1, fixed=False)
    replace_galfit_param('4', rad, object_num=1, fixed=False)

    # object 2 is devauc
    replace_galfit_param('1', centroid, object_num=2, fixed=False)
    replace_galfit_param('3', mag, object_num=2, fixed=False)
    replace_galfit_param('4', rad, object_num=2, fixed=False)

    # create mask file according to the input galaxy
    # NOTE: in Control paramter of input paramfile:
    # F) mask.fits           # Bad pixel mask (FITS image or ASCII coord list)
    cmd = "ic '1 0 %1 0 == ?'  " + ingal + "  > mask.fits"
    subprocess.call(cmd, shell=True)

    # For objects, object_num starts from 1
    # 1 = expdisk, 2 = devauc

    # run galfit
    # rm -r imgblock.fits subcomps.fits galfit.01 # removes these files.
    # galfit sim.feedme  # gives galfit.01, imgblock.fits,if succeed.
    # galfit -o3 galfit.01  # runs only when galfit.01 exists
    # we can delete galfit.01 immediately after it it used.
    cmd1 = 'rm -r imgblock.fits; galfit ' + paramfile
    cmd2 = 'rm -r subcomps.fits; galfit -o3 galfit.01; rm -r galfit.01'
    print("\n\n\n")
    print('*' * 80)
    print('Running: {}'.format(cmd1))
    print('*' * 80)
    subprocess.call(cmd1, shell=True)  # gives galfit.01 if succeed

    if os.path.exists('galfit.01'):

        print("\n\n\n")
        print('!' * 80)
        print('Running: {}'.format(cmd2))
        print('!' * 80)
        subprocess.call(cmd2, shell=True)

    # get residual map from imgblock.fits
    residual = outdir + '/residual/' + galaxy + '_res' + str(count) + '.fits'

    # expdisk from subcomps.fits ext = 1
    expdisk     = outdir + '/expdisk/'     + galaxy + '_expdisk'     + str(count) + '.fits'
    expdisk_res = outdir + '/expdisk_res/' + galaxy + '_expdisk_res' + str(count) + '.fits'

    # devauc from subcomps.fits ext = 2 (NOTE: ext = 1 FOR ONE COMPONET FITTING)
    devauc     = outdir + '/devauc/'     + galaxy + '_devauc'     + str(count) + '.fits'
    devauc_res = outdir + '/devauc_res/' + galaxy + '_devauc_res' + str(count) + '.fits'

    # extracting frames of imgblock.fits and subcomps.fits if they exists.
    if os.path.isfile('subcomps.fits') and os.path.isfile('imgblock.fits'):
        # for imgblock.fits : 0 is empty, 1 is input, 2 is model, 3 is residual
        # for subcomps.fits: 0 is input, 1 is expdisk, 2 is devauc etc.

        # residual
        dat_res, hdr_res = fits.getdata(r'imgblock.fits', ext=3, header=True)
        fits.writeto(residual, dat_res, hdr_res, clobber=True)

        # expdisk
        dat_exp, hdr_exp = fits.getdata(r'subcomps.fits', ext=1, header=True)
        fits.writeto(expdisk, dat_exp, hdr_exp, clobber=True)
        fits.writeto(expdisk_res, dat_exp + dat_res, hdr_exp, clobber=True)

        # devauc
        dat_dev, hdr_dev = fits.getdata(r'subcomps.fits', ext=2, header=True)
        fits.writeto(devauc, dat_dev, hdr_dev, clobber=True)
        fits.writeto(devauc_res, dat_dev + dat_res, hdr_dev, clobber=True)


def main():
    """Main program."""
    # output directory without '/' in the end
    #  there are 302 galaxies for each filter (including 0 to 301)
    galfit_outdir = 'galfit_outputs'
    centroid_f6   = 'centroidsf6.csv'
    centroid_f8   = 'centroidsf8.csv'

    # run galfit for f606w band
    for count in range(0, 1):
        run_galfit('f606w', galfit_outdir, count, centroid_f6)

    # # run galfit for f814w band
    # for count in range(0, 302):
    #     run_galfit('f814w', galfit_outdir, count, centroid_f8)


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
