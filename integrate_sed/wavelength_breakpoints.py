#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : May 31, 2017

# Imports
import time
import numpy as np


#LSST r band wavelength ranges:
#Reference: https://www.lsst.org/sites/default/files/docs/sciencebook/SB_2.pdf
#5520 is the blue side wavelength of LSST r band filter
#6910 is the red  side wavelength of LSST r band filter
#z_g = redshift of original galaxy e.g. 1.5 from config.sh
#lambda are integers with unit Angstrom.
#
#lambda_1 = 5520 / (1 + z_g) = 2208                           
#lambda_2 = 6910 / (1 + z_g) = 2764

z_g = 1.5
lambda_1 = int(5520 / (1 + z_g))                          
lambda_2 = int(6910 / (1 + z_g))
a = np.linspace(2208,2764,num=21,endpoint=True)
a = [int(i) for i in a]
print(a)


#HST wavelength range:
#Reference:
#From http://www.stsci.edu/hst/acs/documents/handbooks/current/c05_imaging2.html
#Camera: HST ACS camera
#Filter  Central          Width  Description  Camera 
#name    wavelength (Å)   (Å)
#F814W   8333             2511   Broad I      WFC/HRC
#
#This gives lambda_hst values:
#For now we choose z_cutout = 0.2
#lambda_hst1  = ( 8333 - (2511/2) ) / (1 + z_cutout) = 7077.5 / 1.2 = 5897.9 
#lambda_hst2  = ( 8333 + (2511/2) ) / (1 + z_cutout) = 9588.5 / 1.2 = 7990.4 

z_cutout = 0.2
lambda_hst1  = int(( 8333 - (2511/2) ) / (1 + z_cutout))
lambda_hst2  = int(( 8333 + (2511/2) ) / (1 + z_cutout))
a = np.linspace(lambda_hst1,lambda_hst2,num=21,endpoint=True)
a = [int(i) for i in a]
print(a)
print('lambda_hst1 = ', lambda_hst1)
print('lambda_hst2 = ', lambda_hst2)
print('lambda1 = ', lambda_1)
print('lambda2 = ', lambda_2)
