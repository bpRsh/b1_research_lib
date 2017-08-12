#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jun 10, 2017 Sat
# Last update : 
#
# Imports
# write to a file
# Imports
import numpy as np
import pandas as pd
from pandas import DataFrame as DF

## Break the data
arr1 = np.array_split(np.arange(301), 7)
df1 = DF(arr1).T
df1.to_csv('tmp.txt',sep='\t',index=None,header=None)

