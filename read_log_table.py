import os
import re
import glob
import pandas as pd

log_table = pd.read_csv('log_table_expdish_f8.csv', sep='\s+', header=None)
log_table2 = pd.read_csv('log_table_expdish_devauc_f8.csv', sep='\s+', header=None)


bad1 = log_table.loc[log_table[7] == 0]
bad2 = log_table2.loc[log_table2[7] == 0]
print(bad1)
print(bad2)
