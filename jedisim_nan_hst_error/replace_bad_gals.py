#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Jun 07, 2017 Wed
# Last update : 
#
#
# Imports
import time
import os
import shutil

bad_gals =  [ '7', '9', '12', '15', '26', '34', '35', '39', '42', '50', 
'55', '61', '62', '64', '65', '66', '72', '77', '78', '94', '96', '99', 
'101', '102', '108', '111', '112', '113', '116', '127', '140', '142', 
'147', '149', '151', '156', '157', '162', '163', '165', '167', '170', 
'173', '174', '178', '179', '186', '188', '189', '190', '193', '195', 
'196', '197', '204', '205', '206', '212', '213', '215', '222', '224', 
'228', '232', '237', '242', '245', '246', '249', '260', '262', '268', 
'271', '272', '276', '277', '286', '287', '296', '297', '298', '300', '301']

def replace_bad_gals():
    """Delete old bad bulge and disk galaxies and create good ones.
    
bad_gals =  [ '7', '9', '12', '15', '26', '34', '35', '39', '42', '50', 
'55', '61', '62', '64', '65', '66', '72', '77', '78', '94', '96', '99', 
'101', '102', '108', '111', '112', '113', '116', '127', '140', '142', 
'147', '149', '151', '156', '157', '162', '163', '165', '167', '170', 
'173', '174', '178', '179', '186', '188', '189', '190', '193', '195', 
'196', '197', '204', '205', '206', '212', '213', '215', '222', '224', 
'228', '232', '237', '242', '245', '246', '249', '260', '262', '268', 
'271', '272', '276', '277', '286', '287', '296', '297', '298', '300', '301']

Delete these bulge and disk galaxies.
Replace bulges by bulge0 and disk by disk11.
    

    """
    # bulge
    for n in bad_gals:
        f = 'bulge_f8/f814w_bulge%s.fits' % n
        print('Replacing: ', f)
        
        # delete and copy bulge
        try:
            os.remove(f)
        except:
            pass
        shutil.copy('bulge_f8/f814w_bulge0.fits', f)
    
    # disk
    for n in bad_gals:
        f = 'disk_f8/f814w_disk%s.fits' % n
        print('Replacing: ', f)
        
        # delete and copy disk
        try:
            os.remove(f)
        except:
            pass
        shutil.copy('disk_f8/f814w_disk11.fits', f)
    




if __name__ == "__main__":
    replace_bad_gals()
