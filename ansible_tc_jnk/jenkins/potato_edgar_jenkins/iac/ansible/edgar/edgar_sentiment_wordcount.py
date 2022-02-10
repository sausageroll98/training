# pylint: disable=W1401
'''
Author: Albert Tran
Created: 2020-08-08

Module to extract sentiment word counts from a a list of 10-k filings in text format.

Example Usage:
--------------
import edgar.edgar_sentiment_wordcount as edgar_sentiment

folder_clean10k = r'C:\temp\junk\10k_reports_clean' # Folder with 10-k text files.
edgar_sentiment.write_document_sentiments(folder_clean10k, r'C:\temp\junk\sentiment_factors.csv')

'''
# pylint: disable=E0401
# pylint: disable=C0411
# %%
# ------------------------------------------------------------------------------
# Negative Sentiment Vectorizer
# ------------------------------------------------------------------------------
import ref_data as edgar_refdata
import os
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from edgar_cleaner import get_10k_file_metadata


# %%
# ------------------------------------------------------------------------------
# Negative Sentiment Vectorizer
# ------------------------------------------------------------------------------
# pylint: disable=C0116
def read_file(file_name):
    # pylint: disable=C0103
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
        df_temp = pd.DataFrame(bag_of_words.sum(axis=1, keepdims=True), columns=[sentiment])
        df_list.append(df_temp)
    # pylint: disable=C0103
    df = pd.concat(df_list, axis=1)
    df['WordCount'] = [len(read_file(f).split(' ')) for f in clean_10k_filenames]

    df.to_json(output_file, index=False)
