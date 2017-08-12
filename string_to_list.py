#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Feb 10, 2019
# Last update :
# Est time    :

# Imports
from natsort import natsorted

a = '218 219 22 124 213 119 184 124 213 119 187 198 209 214 194 200 210 216 148 154 201 211 217 124 125 126 137 138 144 148 150 154 16 168 169 171 172 18 183'
b = [int(i) for i in set(a.split())]
print (natsorted(b))
print(len(b))
