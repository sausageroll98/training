'''
Author : Albert Tran
Created: 2020-08-08

Module to download data from yahoo finance and calculate short-term returns.

Example usage:
df_returns = get_yahoo_data('2000-01-01', '2020-08-01', tickers, 'daily')
df_returns.to_csv(r'C:\\stock_returns_daily.csv', index=False)

'''
# pylint: disable=E0401
# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import pandas as pd
from yahoofinancials import YahooFinancials


# %%
# ------------------------------------------------------------------------------
# Yahoo Finance Data
# ------------------------------------------------------------------------------
def get_yahoo_data(start_date, end_date, tickers, period='daily'):
    '''
    Returns prices and returns for a list of given tickers.
    '''
    # pylint: disable=C0103
    yf      = YahooFinancials(tickers)
    yf_data = yf.get_historical_price_data(start_date, end_date, period)

    list_df = []
    for ticker in yf_data.keys():
        try:
            # Get the data for the relevant ticker
            # pylint: disable=C0301
            df_tmp = pd.DataFrame(yf_data[ticker]['prices'])[['formatted_date', 'high', 'low', 'adjclose', 'volume']]
            df_tmp.rename(columns={'formatted_date':'date', 'adjclose':'price'}, inplace=True)
            for i in [1,2,3,5,10]:
                df_tmp[f'{i}{period}_return'] = df_tmp['price'].pct_change(i).shift(-i)
            df_tmp['Symbol'] = ticker

            list_df.append(df_tmp)
        # pylint: disable=W0702
        except:
            print(f'Data extraction failed for ticker: {ticker}.')
    # pylint: disable=C0103
    df = pd.concat(list_df)
    return df
