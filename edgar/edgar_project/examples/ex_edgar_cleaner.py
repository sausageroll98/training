'''
Author : Albert Tran
Created: 2020-08-08

Examples showing how to use the edgar_cleaner module.
'''

# %%
# ------------------------------------------------------------------------------
# File I/O
# ------------------------------------------------------------------------------
# This assumes that the 10-k .html files have already been written to the input_folder
input_folder  = r'C:\ce02\temp\junk\10k_reports_raw'
output_folder = r'C:\ce02\temp\junk\10k_reports_clean'

# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import sys
sys.path.insert(0,"..")

import edgar_cleaner as cleaner

# %%
# ------------------------------------------------------------------------------
# File I/O
# ------------------------------------------------------------------------------
cleaner.write_clean_html_text_files(input_folder, output_folder)




