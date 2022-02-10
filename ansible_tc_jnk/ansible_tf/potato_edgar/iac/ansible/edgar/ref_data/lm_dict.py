# pylint: disable=C0303

'''
Author : Albert Tran
Created: 2020-08-07

The Loughran-McDonald Master Dictionary can be downloaded here:
https://sraf.nd.edu/textual-analysis/resources/#Master%20Dictionary

Additional documentation:
https://www.uts.edu.au/sites/default/files/ADG_Cons2015_Loughran%20McDonald%20JE%202011.pdf

'''

# %% 
# ------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import os
# pylint: disable=import-error
import pandas as pd
import pkg_resources


# %% 
# ------------------------------------------------------------------------------
# File Path
#-------------------------------------------------------------------------------
# Setting up the file path
DATA_PATH = pkg_resources.resource_filename(__name__, '../ref_data/csv/')
file_path = os.path.join(DATA_PATH,'LoughranMcDonald_MasterDictionary_2018.csv')


# %% 
# ------------------------------------------------------------------------------
# Loughran-McDonald Dictionary
#-------------------------------------------------------------------------------
sentiment_list = ['Negative','Positive','Uncertainty','Litigious',
                  'Constraining','Superfluous','Interesting','Modal']


def get_lmdict_df(lemmatize=False, relevant_cols_only=True):
    '''
    Returns the LM dictionary as a table.
    '''
    # Read in the data path
    # pylint: disable=invalid-name
    df = pd.read_csv(file_path)
    # pylint: disable=fixme
    # TODO: Figure out what the numbers in the cells mean...

    # Remove irrelevant columns
    if relevant_cols_only:
        df = df[['Word'] + sentiment_list]
    
    # Remove words that are not associated with any sentiment
    df[sentiment_list] = df[sentiment_list].astype(bool)
    df = df[df[sentiment_list].any(axis=1)]

    # Change all words to lowercase
    df['Word'] = df['Word'].str.lower()

    # Lemmatization
    if lemmatize:
        # TODO: Lemmatization and duplicate dropping?
        print('Implement lemmatization!')
        # pylint: disable=unnecessary-pass
        pass

    return df


def get_sentiment_word_dict(**params):
    '''
    Returns a dictionary where:
    - The keys are the sentiments
    - The value is a list of words associated with the sentiments
    '''
    # Get the LM table
    # pylint: disable=invalid-name
    df = get_lmdict_df(**params)

    # Create the sentiment dictionary
    sentiment_dict = {}
    for sentiment in sentiment_list:
        sentiment_dict[sentiment] = df[df[sentiment]]['Word'].tolist()
    
    return sentiment_dict
