'''
Author : Albert Tran
Created: 2020-08-10

'''

# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %%
# ------------------------------------------------------------------------------
# File I/O
# ------------------------------------------------------------------------------
df_sentiment = pd.read_csv(r'C:\ce02\temp\junk\sentiment_factors.csv')
df_returns   = pd.read_csv(r'C:\ce02\temp\junk\stock_returns_daily.csv')






# %%
# ------------------------------------------------------------------------------
# File Reading / Pre-Processing
# ------------------------------------------------------------------------------
# Merging dataframes and dropping nulls
df = pd.merge(df_sentiment, df_returns, how='inner', 
              left_on=['FilingDate', 'Symbol'], right_on=['Date', 'Symbol'])
df.dropna(inplace=True)

# Creating new columns
df['volume_norm']        = (df['volume'] - df.groupby('Symbol')['volume'].transform(np.mean)) / df.groupby('Symbol')['volume'].transform(np.std)
df['NegGroup']           = pd.qcut(df.Negative, 5)
df['NegativeRatio']      = df['Negative']/(df['WordCount']+1)
df['NegativeToPositive'] = df['Negative']/(df['Positive']+1)



# %%
# ------------------------------------------------------------------------------
# Analysis
# ------------------------------------------------------------------------------
return_cols = [c for c in df.columns if c.endswith('_return')]
df.groupby(['NegGroup'])[return_cols].median()
df.groupby(['NegGroup'])['volume'].median()
df.groupby(['NegGroup'])['volume_norm'].median()






