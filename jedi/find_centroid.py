#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Feb 9, 2017
# Last update : Feb 11, 2017
# Est time    : 34 seconds (maximum)

# Imports
from astropy.io import fits
import numpy as np
import pandas as pd
import os
import glob
import re


def natural_sort_datafile(infile, outfile):
    """Sort data file naturally according first column."""
    df = pd.read_csv(infile, sep=' ', skipinitialspace=True, header=None)
    df.sort_values(by=[0], inplace=True)
    df.to_csv(outfile, header=None, index=None, sep=' ')
    return None


def find_centroid(fitsfile):
    """Find centroid of the fitsfile."""
    dat1 = fits.getdata(fitsfile)
    dat = dat1
    indices = np.where(dat == dat.max())
    y1, x1 = list(zip(indices[0], indices[1]))[0]  # first maximum value of matrix
    y1, x1 = y1 + 1, x1 + 1
    max1 = [x1, y1]

    # to find second max, make maximum value zero and repeat above process
    dat[indices] = 0.0
    indices = np.where(dat == dat.max())
    y2, x2 = list(zip(indices[0], indices[1]))[0]  # first maximum value of matrix
    y2, x2 = y2 + 1, x2 + 1
    max2 = [x2, y2]

    # to find second max, make maximum value zero and repeat above process
    dat[indices] = 0.0
    indices = np.where(dat == dat.max())
    y3, x3 = list(zip(indices[0], indices[1]))[0]  # first maximum value of matrix
    y3, x3 = y3 + 1, x3 + 1
    max3 = [x3, y3]

    # to find second max, make maximum value zero and repeat above process
    dat[indices] = 0.0
    indices = np.where(dat == dat.max())
    y4, x4 = list(zip(indices[0], indices[1]))[0]  # first maximum value of matrix
    y4, x4 = y4 + 1, x4 + 1
    max4 = [x4, y4]

    # print
    return max1, max2, max3, max4


def write_centroid(in_pth, out_centroid):
    """Write centroid file into a file reading from given path.
    e.g.
    in_pth = '/Users/poudel/jedisim/simdatabase/galaxies/f6*.fits'
    out_centroid = 'centroidsf6.csv'

    To do natural sorting:
    open centroidsf6.csv in atom editor
    select all
    Packages > Sorter > Natural sorting

    """
    with open('temp.csv', 'w') as fout:
        for f in glob.glob(in_pth):
            max1, max2, max3, max4 = find_centroid(f)
            num = re.search('(.+?)(\d+)(\.\w*)', f).group(2)
            print(num, max1[0], max1[1], max2[0], max2[1],
                  max3[0], max3[1], max4[0], max4[1], file=fout)
    # natural sort temp file
    natural_sort_datafile('temp.csv', out_centroid)

    # now, delete temp
    if os.path.isfile('temp.csv'):
        os.remove('temp.csv')
        pass


def main():
    """Run main function."""
    # f606w
    in_pth = '/Users/poudel/jedisim/simdatabase/galaxies/f6*.fits'
    out_centroid = 'centroidsf6_four.csv'
    centroids = 'centroidsf6.csv'
    write_centroid(in_pth, out_centroid)

    # write only 1 maxima
    df = pd.read_csv(out_centroid, sep=' ', skipinitialspace=True, header=None)
    df2 = df.loc[:, [0, 1, 2]]
    df2.to_csv(centroids, header=None, index=None, sep=' ')

    # f814w
    in_pth = '/Users/poudel/jedisim/simdatabase/galaxies/f8*.fits'
    out_centroid = 'centroidsf8_four.csv'
    centroids = 'centroidsf8.csv'
    write_centroid(in_pth, out_centroid)

    # write only 1 maxima
    df = pd.read_csv(out_centroid, sep=' ', skipinitialspace=True, header=None)
    df2 = df.loc[:, [0, 1, 2]]
    df2.to_csv(centroids, header=None, index=None, sep=' ')


if __name__ == "__main__":
    import time

    # beginning time
    program_begin_time = time.time()
    begin_ctime = time.ctime()

    #  Run the main program
    main()

    # print the time taken
    program_end_time = time.time()
    end_ctime = time.ctime()
    seconds = program_end_time - program_begin_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print("nBegin time: ", begin_ctime)
    print("End   time: ", end_ctime, "\n")
    print("Time taken: {0: .0f} days, {1: .0f} hours, \
      {2: .0f} minutes, {3: f} seconds.".format(d, h, m, s))
