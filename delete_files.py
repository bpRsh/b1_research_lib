#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
import os
import subprocess


def delete_files(filenames):
    """Try delete a file."""
    for f in filenames:
        if os.path.isfile(f):
            os.remove(f)
        else:
            print('FILE NOT FOUND: ', f)

delete_files(['mask.fits', 'imgblock.fits',  'subcomps.fits'])
