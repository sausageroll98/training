'''
Author : Albert Tran
Created: 2020-08-10

'''

# %%
# ------------------------------------------------------------------------------
# File I/o
# ------------------------------------------------------------------------------
folder_raw        = r'C:\ce02\temp\junk\10k_reports_raw'
folder_clean      = r'C:\ce02\temp\junk\10k_reports_clean'
sentiment_file    = r'C:\ce02\temp\junk\sentiment_factors.csv'
stockreturns_file = r'C:\ce02\temp\junk\stock_returns_daily.csv'

# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import sys
sys.path.insert(0,"..")

import edgar_downloader as edgar_downloader
import edgar_cleaner as edgar_cleaner
import ref_data as edgar_refdata
import edgar_sentiment_wordcount as edgar_sentiment
import ref_data as edgar_refdata

import matplotlib.pyplot as plt
import pandas as pd

# %%
# ------------------------------------------------------------------------------
# 0. Specify our stock universe
# ------------------------------------------------------------------------------
df_sp100 = edgar_refdata.get_sp100()
#tickers  = df_sp100['Symbol']
tickers  = ['MSFT','AAPL', 'CVX', 'FB', 'WMT'] #Smaller subset


# %%
# ------------------------------------------------------------------------------
# 1. Download raw 10-k html files
# ------------------------------------------------------------------------------
# Download the data for each ticker
# Note that the full S&P100 takes around 50 minutes to run.
for i, ticker in enumerate(tickers):
    print(f'{(i/len(tickers))*100}% complete. Current ticker: {ticker}.')
    edgar_downloader.download_files_10k(ticker, folder_raw)
    print('--------------------------------')

print('done')



# %%
# ------------------------------------------------------------------------------
# 2. Clean Files
# ------------------------------------------------------------------------------
edgar_cleaner.write_clean_html_text_files(folder_raw, folder_clean)


# %%
# ------------------------------------------------------------------------------
# 3. Get Market data
# ------------------------------------------------------------------------------
df_returns = edgar_refdata.get_yahoo_data('2000-01-01', '2020-08-01', tickers)


# %%
# ------------------------------------------------------------------------------
# 4. Extract sentiment word counts
# ------------------------------------------------------------------------------
edgar_sentiment.write_document_sentiments(folder_clean, sentiment_file)



# %%
# ------------------------------------------------------------------------------
# 5. Join sentiment data to market data
# ------------------------------------------------------------------------------
df_sentiment = pd.read_csv(sentiment_file)
# df_returns   = pd.read_csv(stockreturns_file)

df = pd.merge(df_sentiment, df_returns, how='inner', 
              left_on=['FilingDate', 'Symbol'], right_on=['date', 'Symbol'])
df.dropna(inplace=True)


# Plotting negative sentiment vs volume (ILLUSTRATION ONLY)
fig, ax = plt.subplots()
ax.scatter(df['Negative'], df['volume'])
ax.grid()
ax.set_xlabel('Negative Sentiment')
ax.set_ylabel('Volume')

# Plotting negative sentiment vs volume (ILLUSTRATION ONLY)
fig, ax = plt.subplots()
ax.scatter(df['Negative'], df['3daily_return'])
ax.grid()
ax.set_xlabel('Negative Sentiment')
ax.set_ylabel('3-day Return')




