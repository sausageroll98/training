'''
Author : Albert Tran
Created: 2020-08-07

Examples showing how to download 10-k reports using the edgar_downloader module.
'''

# %%
# ------------------------------------------------------------------------------
# File I/O
# ------------------------------------------------------------------------------
# This is the folder where the reports will be downloaded
data_dir = r'C:\ce02\temp\junk\10k_reports_raw'


# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import sys
sys.path.insert(0,"..")

import edgar_downloader as edgar_downloader
import ref_data as edgar_refdata

from tqdm import tqdm


# %%
# ------------------------------------------------------------------------------
# 10-k File Download (Full Download pf S&P100)
# ------------------------------------------------------------------------------
# Specify the company whose 10-k reports we are interested in.
df_sp100 = edgar_refdata.get_sp100()
tickers  = df_sp100['Symbol']
tickers = ['MSFT']
# tickers  = ['MSFT', 'AAPL', 'CVX', 'FB', 'WMT'] # smaller subset

# Download the data for each ticker
# Note that this takes around 50 minutes to run.
for i, ticker in enumerate(tickers):
    print(f'{((i+1)/len(tickers))*100}% complete. Current ticker: {ticker}.')
    edgar_downloader.download_files_10k(ticker, data_dir)
    print('--------------------------------')

print('done')


