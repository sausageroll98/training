'''
Author: Albert Tran
Created: 2020-08-08

Module to get S&P500 reference data. Data is a snapshot taken from:
https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
'''

# %% 
# ------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import os
import pandas as pd
import pkg_resources


# %% 
# ------------------------------------------------------------------------------
# File Path
#-------------------------------------------------------------------------------
# Setting up the file path
DATA_PATH = pkg_resources.resource_filename(__name__, '../ref_data/csv/')
file_path_sp100 = os.path.join(DATA_PATH,'sp100_companies.csv')
file_path_sp500 = os.path.join(DATA_PATH,'sp500_companies.csv')


# %% 
# ------------------------------------------------------------------------------
# Data read
#-------------------------------------------------------------------------------
def get_sp500():
    return pd.read_csv(file_path_sp500)


def get_sp100():
    df_sp100 = pd.read_csv(file_path_sp100)
    df_sp500 = get_sp500()
    return df_sp500[df_sp500['Symbol'].isin(df_sp100['Symbol'])]

