#!/usr/local/bin/env python3
import natsort
import pandas as pd
from iteration_utilities import duplicates
from iteration_utilities import unique_everseen

a = [18, 212, 282, 289, 300, 18]
b = [10, 102, 111, 282, 18]
allnums = a + b

# # method 1
# all_dups = [x for x in allnums if allnums.count(x) > 1]
# dups = list(set(all_dups))
# print(all_dups)
# print(dups)
#
# # using pandas
# vc = pd.Series(allnums).value_counts()
# dups = vc[vc > 1].index.tolist()
# print(dups)
#
#
# # using pandas
# dups = pd.Series(allnums)[pd.Series(allnums).duplicated()].values
# print(dups)
#
# using library
dups = list(duplicates(allnums))
dups_unq = list(unique_everseen(duplicates(allnums)))
print(dups)
print(dups_unq)
