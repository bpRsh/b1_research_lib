#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : May 10, 2017 Wed
# Last update :
# Est time    :
#
# Imports
import os
import glob
import re


# Rename galaxies to bulge_f8
def rename_bulge_f8_missing_headers():
    """Rename files inside bulge_f8_missing_headers.
    
    It will replace base filename gal to bulge.
    
    Note: the list files is not natural alphanumerical, its alphabetical.
    i.e. the last file to convert is f814w_gal99.fits not 301.fits
    
    """
    files = glob.glob('bulge_f8_missing_headers/*.fits')
    for f in files:
        try:
            f2 = f.replace('bulge_f8_missing_headers/f814w_gal',
                           'bulge_f8_missing_headers/f814w_bulge')
            os.rename(f, f2)
            print("\n")
            print('From: ', f)
            print('To  : ', f2)
        except:
            pass


# Rename devauc_res to bulge
def rename_devauc():
    files = glob.glob('devauc/*.fits')
    for f in files:
        try:
            f2 = f.replace('devauc/f814w_devauc', 'devauc/f814w_bulge')
            os.rename(f, f2)
            print("\n")
            print('From: ', f)
            print('To  : ', f2)
        except:
            pass

# Rename expdisk_res to disk
def rename_expdisk_res():
    files = glob.glob('expdisk_res/*.fits')
    for f in files:
        try:
            f2 = f.replace('expdisk_res/f814w_expdisk_res', 'expdisk_res/f814w_disk')
            os.rename(f, f2)
            print("\n")
            print('From: ', f)
            print('To  : ', f2)
        except:
            pass


if __name__ == '__main__':
    #rename_bulge_f8_missing_headers()
    #rename_devauc()
    rename_expdisk_res()
