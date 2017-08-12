#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jul 06, 2017 Thu
# Last update :



def natural_sort_datafile(infile, outfile):
    """Sort data file naturally according first column."""
    df = pd.read_csv(infile, sep=' ', skipinitialspace=True, header=None)
    df.sort_values(by=[0], inplace=True)
    df.to_csv(outfile, header=None, index=None, sep=' ')
    return None


if __name__ == "__main__":
    infile = '/Users/poudel/Research/useful_scripts_lib/centroidsf6.csv'
    outfile = 'centroids_sorted_f6.csv'
    natural_sort_datafile(infile, outfile)
