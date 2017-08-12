# Author    : Bhishan Poudel
# Date      : Jun 07, 2017 Wed

# Topic: Creation of folders galaxies, bulge_f8 and disk_f8 for jedimaster

a.  Preprocess original galaxies
    ============================
    From: /Users/poudel/jedisim/simdatabase/stamps_f8
    To  : /Users/poudel/jedisim/simdatabase/galaxies
    
    downloaded folders : stamps_old, stamps_new
    
    i. bad tabbed headers file: f814w_gal202.fits
        fix bad tabbed header file first
        move this file to stamps_bad
	correct it, and copy good file inside stamps_f8.
	using fix_bad_tabbed_headers.py
	
    ii. bad BYTEORDR problem: all 302 original galaxies has this problem.
        fix bad byteordr problem.
	using fix_bad_byteordr.py
	
    End: In the end the folder "galaxies" has good 302 f814 fitsfiles.

b.  Create masks to multiply with devauc and expdisk_res
    =====================================================
    After preprocessing errors in original galaxies, create masks for 
    these 302 galaxies using create_mask_for_gals.py


c.  Create bulge_f8
    ========================

    First create:
    ~/jedisim/simdatabase/devauc_masked
    (bulge_f8 will be created by multiply_mask_bulge_disk.py)

    For the folder galaxies, make sure that all the f814 files have good headers
    with keywords MAG, MAG0, RADIUS, and PIXSCALE using read_headers.py since
    jedicatalog needs these keywords.



    Duplicate folder galaxies into name bulge_f8_missing_headers.
    from: galaxies
    to  : bulge_f8_missing_headers.

    Now we have 302 galaxies in bulge_f8_missing_headers.
    Rename gal ==> bulge using rename_files.py

    We are only using f814, not f606 since the latter gave bad two
    component fitting in galfit.


    Copy the folder devauc NOT devauc_res
    The folder devauc has 264 files.
    From:  /Users/poudel/Research/galfit_usage/expdisk_devauc/
            galfit_outputs_f8/devauc

    To  : /Users/poudel/jedisim/simdatabase/devauc

    Rename all the files in simdatabase/devauc
    From  : devauc/f814w_devauc0.fits
    To    : devauc/f814w_bulge0.fits
    Using : rename_files.py with some edit.
    
    Copy all these 264 files from devauc to bulge_f8_missing_headers
    and replace old ones. (DO NOT DUPLICATE FOLDER)
    
    The files copied from galaxies to bulge_f8_missing_headers
    have required four headers.

    However, the files copied from devauc to bulge_f8_missing_headers
    do not have the headers MAG MAG0 RADIUS PIXSCALE
    and these keywords are required by jedicatalog.

    So, we will add these headers to all 302 files using add_headers.py.    
    
    Now the folder bulge_f8_unmasked has 302 unmasked f814w files.
    We multiply these files with the mask and write into bulge_f8
    using multiply_mask_bulge_disk.py.

   
    

    WARNING:
    =======

    While using add_headers.py I encountered bad BYTEORDR (not BYTEORDER)
    problem.
    The first fitsfile bulge_f8/f814w_bulge0.fits was successful but
    galaxy1 was failed.

    The bulge0 was from devauc which has no any header keyword BYTEORDR.
    The bulge1 was from original galaxies downloaded from web.

    Using ds9 I opened the bulge0 and bulge1,
    bulge0 has no header keyword named BYTEORDR.

    However, bulge1 had BYTEORDR value without quotes around it.
    BYTEORDR=           BIG_ENDIAN / SunOS, solaris etc. byte order

    I checked other original galaxies they also have the same problem.
    So I wrote a code fix_byteordr.py to fix the problem.

    However, I again encountered bad tabbed header keywords
    (FLUX\t MAG\t RADIUS\t) in one of the 302 files, viz., f814w_gal202.fits.
    To fix this problem I wrote a code fix_bad_tabbed_headers.py.

    In summary,
    first run fix_bad_tabbed_headers.py
    then  run fix_bad_byteordr.py.


    Fix bad headers of original galaxies (from stamps_all to galaxies)
    ====================================================================
    From: /Users/poudel/jedisim/simdatabase/stamps_f8
    To  : /Users/poudel/jedisim/simdatabase/galaxies

    First run fix_bad_tabbed_headers.py
    Then  run fix_bad_byteordr.py.

Nutshell:
=========
create    ~/jedisim/simdatabase/bulge_f8_missing_headers
create    ~/jedisim/simdatabase/bulge_f8

copy 302 files from galaxies to bulge_f8_missing_headers and rename them.
copy files from two-comp devauc to here devauc_res and rename them.
copy and replace files from devauc to bulge_f8_missing_headers.
add headers to all these 302 files into folder bulge_f8.


d. To create disk files
    ===================
    cd ~/jedisim/dev/dev_simdatabase
    create  disk_f8_unmasked


    Create a folder callled "disk_f8_missing_headers" with 302 null fitsfiles
    of size 601 601 using script "create_null_fitsfile.py"

    Copy folder expdisk_res from two component fitting to here.

    From:  /Users/poudel/Research/galfit_usage/expdisk_devauc/
            galfit_outputs_f8/expdisk_res

    To  : /Users/poudel/jedisim/dev/dev_simdatabase/expdisk_res

    Rename files from expdisk_res to disk using rename_files.py.

    Copy and replace 264 files from expdisk_res into disk_f8_missing_headers.
    (302 - 264 = 38 missing disk will be null fitsfiles)

    Add four headers to these null fitsfiles from galaxies using
    add_headers.py which will create files in disk_f8_unmasked.
    
    Now we add the mask to these images using multiply_mask_bulge_disk.py
    and final disk images will be written inside disk_f8.

