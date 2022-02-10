'''
Author : Albert Tran
Created: 2020-08-08

Module for trying out and testing stuff.


'''

# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------


import ref_data as edgar_data


# %%
# ------------------------------------------------------------------------------
# 
# ------------------------------------------------------------------------------
df_sp500 = edgar_data.get_sp500()


sentiment_words = edgar_data.get_sentiment_word_dict()

'''
Project Components:
- Downloader
- Section Extractor
- Unit Tests

NLP. For each document, we need to:
- Do a word count for the number of negative words.
- Get the readability score.
- Join this back to stock price data.
- See if there is a correlation.

'''


def get_10k_html_metadata_old(html_file_path):
    '''
    Given the full path to a html filing, returns the metadata.
    Input file is expected to be in the following format:
        <ticker>_10-k_<filing_date>.
    If file is not in the correct format, None is returned.
    '''
    # Check if the file is in the correct format
    html_file = os.path.basename(html_file_path)
    file_bits = html_file.split('_')
    if (len(file_bits) != 3) or (not html_file.endswith('html')):
        return None

    # Return the metadata for the file
    ticker, report_type, filing_date = file_bits
    return (ticker, report_type, filing_date.split('.')[0])





# %%
# ------------------------------------------------------------------------------
# Negative Sentiment Vectorizer
# ------------------------------------------------------------------------------
import edgar.ref_data as edgar_refdata
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from edgar.edgar_cleaner import get_10k_file_metadata

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def write_document_sentiments(input_folder, output_file):
    '''
    Writes a table containing the counts of sentiment words for each document.

    Arguments:
    ----------
    input_folder: folder containing cleaned 10-k text files.
    output_file : file 
    '''
    clean_10k_filenames = [os.path.join(input_folder, f) for f in \
                           os.listdir(input_folder) if f.endswith('.txt')]

    # For each file, keep track of the ticker and filing date.
    clean_10k_meta    = [get_10k_file_metadata(f) for f in clean_10k_filenames]
    df_clean_10k_meta = pd.DataFrame(clean_10k_meta, columns=['Symbol', 'ReportType', 'FilingDate'])
    df_list           = [df_clean_10k_meta]

    # Read in file contents
    clean_10k_corpus = [read_file(f) for f in clean_10k_filenames]
    sentiment_dict   = edgar_refdata.get_sentiment_word_dict()

    # Tally up the number of words for each sentiment
    for sentiment, sentiment_words in sentiment_dict.items():
        print('Current sentiment: ', sentiment)
        vectorizer   = CountVectorizer(vocabulary=sentiment_words)
        bag_of_words = vectorizer.fit_transform(clean_10k_corpus).toarray()

        df_temp = pd.DataFrame(bag_of_words, columns=sentiment_words)
        df_temp = pd.DataFrame(bag_of_words.sum(axis=1, keepdims=True), columns=['sentiment'])
        df_list.append(df_temp)

    df = pd.concat(df_list, axis=1)
    df['WordCount'] = [len(read_file(f).split(' ')) for f in clean_10k_filenames]

    df.to_csv(output_file, index=False)


folder_clean10k = r'D:\temp\junk\10k_reports_clean'
write_document_sentiments(folder_clean10k, r'D:\temp\junk\sentiment_factors.csv')




# %%




folder_clean10k = r'D:\temp\junk\10k_reports_clean'
clean_10k_filenames = [os.path.join(folder_clean10k, f) for f in \
                       os.listdir(folder_clean10k) if f.endswith('.txt')]

clean_10k_corpus = [read_file(f) for f in clean_10k_filenames]
clean_10k_meta   = [get_10k_file_metadata(f) for f in clean_10k_filenames]

sentiment_dict = edgar_refdata.get_sentiment_word_dict()
negative_words = sentiment_dict['Negative']

vectorizer   = CountVectorizer(vocabulary=negative_words)
bag_of_words = vectorizer.fit_transform(clean_10k_corpus).toarray()
print(bag_of_words.shape)


df_test = pd.DataFrame(bag_of_words, columns=negative_words)
neg_word_count = pd.DataFrame(bag_of_words.sum(axis=1, keepdims=True), columns=['NegWordCount'])

df_clean_10k_meta = pd.DataFrame(clean_10k_meta, columns=['Symbol', 'ReportType', 'FilingDate'])
df = pd.concat([df_clean_10k_meta, neg_word_count], axis=1)
df['WordCount'] = [len(read_file(f).split(' ')) for f in clean_10k_filenames]

df.to_csv(r'D:\temp\junk\sentiment_factors.csv', index=False)











# %%
# ------------------------------------------------------------------------------
# Download Returns Data
# ------------------------------------------------------------------------------
import edgar.ref_data as edgar_refdata
import pandas as pd

from yahoofinancials import YahooFinancials

tickers = edgar_refdata.get_sp100()['Symbol'].tolist()

yf = YahooFinancials(tickers)
blah = yf.get_historical_price_data('2000-01-01', '2020-08-01', 'daily')

list_df = []
for ticker in blah.keys():
    try:
        df_tmp = pd.DataFrame(blah[ticker]['prices'])[['formatted_date', 'high', 'low', 'adjclose', 'volume']]
        df_tmp.rename(columns={'formatted_date':'date', 'adjclose':'price'}, inplace=True)
        for days in [1,2,3,5,10]:
            df_tmp[f'{days}day_return'] = df_tmp['price'].pct_change(days).shift(-days)
        df_tmp['Symbol'] = ticker

        list_df.append(df_tmp)
    except:
        print(f'Data extraction failed for ticker: {ticker}.')

df_returns = pd.concat(list_df)
df_returns.to_csv(r'D:\temp\junk\stock_returns_daily.csv', index=False)

def get_yahoo_data(start_date, end_date, tickers, period='daily'):
    '''
    Returns prices and returns for a list of given tickers.
    '''
    yf      = YahooFinancials(tickers)
    yf_data = yf.get_historical_price_data(start_date, end_date, period)

    list_df = []
    for ticker in yf_data.keys():
        try:
            # Get the data for the relevant ticker
            df_tmp = pd.DataFrame(yf_data[ticker]['prices'])[['formatted_date', 'high', 'low', 'adjclose', 'volume']]
            df_tmp.rename(columns={'formatted_date':'date', 'adjclose':'price'}, inplace=True)
            for i in [1,2,3,5,10]:
                df_tmp[f'{i}{period}_return'] = df_tmp['price'].pct_change(i).shift(-i)
            df_tmp['Symbol'] = ticker

            list_df.append(df_tmp)
        except:
            print(f'Data extraction failed for ticker: {ticker}.')

    df = pd.concat(list_df)
    return df

# Contains 500,000 rows
df_returns = get_yahoo_data('2000-01-01', '2020-08-01', tickers, 'daily')
df_returns.to_csv(r'D:\temp\junk\stock_returns_daily.csv', index=False)




# %%
# ------------------------------------------------------------------------------
# Compare to Returns
# ------------------------------------------------------------------------------
import pandas as pd

df_sentiment = pd.read_csv(r'D:\temp\junk\sentiment_factors.csv')

df_returns   = pd.read_csv(r'D:\temp\junk\stock_returns_daily.csv')


df = pd.merge(df_sentiment, df_returns, how='inner', 
              left_on=['FilingDate', 'Symbol'], right_on=['date', 'Symbol'])

df.dropna(inplace=True)

import numpy as np
df['volume_norm'] = (df['volume'] - df.groupby('Symbol')['volume'].transform(np.mean)) / df.groupby('Symbol')['volume'].transform(np.std)


df['NegGroup'] = pd.qcut(df.Negative, 5)

df['NegativeRatio']      = df['Negative']/(df['WordCount']+1)
df['NegativeToPositive'] = df['Negative']/(df['Positive']+1)

return_cols = [c for c in df.columns if c.endswith('_return')]
df.groupby(['NegGroup'])[return_cols].median()
df.groupby(['NegGroup'])['volume'].median()
df.groupby(['NegGroup'])['volume_norm'].median()

df_sentiment.shape
df_returns.shape
df.shape





df[['NegWordCount', 'volume', '1daily_return', ]]

len(df)

df_corr = df.corr(method='spearman')
df_temp = df_corr[['Negative', 'NegativeRatio', 'NegativeToPositive']]

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(df['Negative'], df['3daily_return'], alpha=0.1)
ax.grid()


fig, ax = plt.subplots()
ax.scatter(df['Negative'], df['volume'], alpha=0.1)
ax.grid()


fig, ax = plt.subplots()
ax.scatter(df['Negative'], df['volume_norm'], alpha=0.1)
ax.grid()


# %%
