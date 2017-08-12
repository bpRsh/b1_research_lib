#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jul 06, 2017 Thu
# Last update :


def main():
    """Main Module."""
    # Imports
    import os
    import re
    import glob
    from natsort import natsorted

    line = ' expdisk   : (  314.27,   306.99)   *23.93*     48.80    0.89   -34.97'

    num_list = list(map(float, re.findall(r"""(?:-)?   # negative
                                   \d+                 # digits
                                   (?:\.\d+)?          # decimal part
                                   """, line, re.X)))  # re.VERBOSE

    print(num_list)
    

if __name__ == '__main__':
    main()

