'''
Author : Albert Tran
Created: 2020-08-08

'''

# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import edgar.ref_data as edgar_data


# %%
# ------------------------------------------------------------------------------
# Getting reference data
# ------------------------------------------------------------------------------
# %%
# S&P Data
df_sp100 = edgar_data.get_sp100()
print(df_sp100)

df_sp500 = edgar_data.get_sp500()
print(df_sp500)



# %%
# Loughran-McDonald word list data
sentiment_words = edgar_data.get_sentiment_word_dict()
print(sentiment_words)

df_lmdict = get_lmdict_df()
print(df_lmdict)



# %%
# Yahoo Data
tickers = ['AAPL', 'MSFT', 'AMZN']
tickers = df_sp100.Symbol
df_returns = edgar_data.get_yahoo_data('2000-01-01', '2020-08-01', tickers, 'daily')
df_returns.to_csv(r'D:\temp\junk\stock_returns_daily.csv', index=False)
