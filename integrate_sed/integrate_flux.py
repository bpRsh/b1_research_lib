#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : May 31, 2017
# Last update : 
# Info        : This program integrates the flux column for 6 Gyr and 12 Gyr
#               stars from the given sed file.
#
# Final Need  : I have to find the two arguments for jedicolor program, viz., 
#m = nr_b / dr_b
#m1 = nr_d / dr_d

#where,
#nr = nr_b = nr_d = LSST r band filter narrowbands between 2208 and 2764
#dr_b = Ihb12 / N

#where,
#lambda_1     = 5520 / (1 + z_g)  = 2208                           
#lambda_2     = 6910 / (1 + z_g)  = 2764
#lambda_hst1  = ( 8333 - (2511/2) ) / (1 + z_cutout) = 7077.5 / 1.2 = 5897.9 = 5898 
#lambda_hst2  = ( 8333 + (2511/2) ) / (1 + z_cutout) = 9588.5 / 1.2 = 7990.4 = 7990

#Ilb6  = integrate_lambda1_to_lambda2  for ssp_6
#Ild6  = integrate_lambda1_to_lambda2  for exp9_6
#Ihb12 = integrate_lambda_hst1_to_hst2 for ssp_12 
#Ihd12 = integrate_lambda_hst1_to_hst2 for exp9_12 

#5520 = blue end of LSST r band filter
#6910 = red  end of LSST r band filter
#8333 = central wavelength  of F814W filter for HST ACS camera
#2511 = width of wavelenght of F814W filter for HST ACS camera
#
# Imports
import numpy as np
import pandas as pd
from scipy.integrate import simps

infileb     = "ssp_pf_interpolated.csv"
infiled     = "exp9_pf_interpolated.csv"

columns = ['wav','flux6','flux12']
dfb = pd.read_csv(infileb, sep=r'\s+',names=columns)
dfd = pd.read_csv(infiled, sep=r'\s+',names=columns)


dfb2  = dfb[(dfb['wav']>=2208) & (dfb['wav']<=2764)]
dfd2  = dfd[(dfd['wav']>=2208) & (dfd['wav']<=2764)]
dfhb2 = dfb[(dfb['wav']>=5898) & (dfb['wav']<=7990)]
dfhd2 = dfd[(dfd['wav']>=5898) & (dfd['wav']<=7990)]
#print(dfhb2.head())
#print(dfhb2.tail())

flb6  = dfb2['flux6']
fld6  = dfd2['flux6']
fhb12 = dfhb2['flux12']
fhd12 = dfhd2['flux12']

print(flb6.head())
print(fld6.head())
print(fhb12.head())
print(fhd12.head())


Ilb6  = simps(flb6)
Ild6  = simps(fld6)
Ihb12 = simps(fhb12)
Ihd12 = simps(fhd12)

print("\n")
print('Ilb6 = ', Ilb6)
print('Ild6 = ', Ild6)
print('Ihb12 = ', Ihb12)
print('Ihb12 = ', Ihd12)
print("\n")

N    = (Ilb6 + Ild6) / (Ihb12 + Ihd12)
dr_b = Ihb12 / N
dr_d = Ihd12 / N

print('N = ', N)
print('dr_b = ', dr_b)
print('dr_d = ', dr_d)

#### The End ###
