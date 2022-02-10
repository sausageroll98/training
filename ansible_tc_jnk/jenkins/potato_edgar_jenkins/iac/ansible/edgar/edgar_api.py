'''To set up uvicorn:
# uvicorn edgar_api:app --reload
'''
# pylint: disable=E0401
# pylint: disable=C0413
# pylint: disable=C0103
# pylint: disable=W0613
# pylint: disable=W0611
# pylint: disable=C0411
import sys
sys.path.insert(0, '.')

import os
import ref_data as edgar_refdata
import edgar_downloader
import edgar_cleaner as cleaner
from fastapi import FastAPI




app = FastAPI()

@app.get("/")
async def root():
    '''STARTING UP API'''
    return {"message": "Edgar is alive."}


@app.get("/html/{ticker}/{year}")
async def get_html(ticker, year):
    '''API FUNCTION TO GET HTML'''
    year = int(year)
    ticker = ticker.upper()
    tickers = edgar_refdata.get_sp100()['Symbol'].tolist()
    input_folder = r'/tmp/potato/10k_reports_raw'

    # pylint: disable=C0301
    # pylint: disable=R1721
    html_files = [f for f in os.listdir(input_folder)] # if (get_10k_file_metadata(f) and f.endswith('.html'))]

    if year < 2000 or year > 2021:
        return {"ERROR": f"year {year} is invalid"}
    if ticker not in tickers:
        return {"Error": f"ticker {ticker} not recognised"}

    inFolder = False
    for i in html_files:
        if ticker in i and str(year) in i:
            inFolder = True
            fileName = i
    if inFolder is False:
        #pylint: disable = invalid-name
        #pylint: disable = unused-variable

        (success, responseMsg) = edgar_downloader.download_files_10k(ticker, input_folder, str(year))
        print('--------------------------------')
        html_files = [f for f in os.listdir(input_folder)]
        for i in html_files:                            # make into function
            if ticker in i and str(year) in i:          #
                inFolder = True                         #
                fileName = i                            #

    localUrl = fr'{input_folder}/{fileName}' # input_folder + '\\' + fileName
    # pylint: disable=W1514
    with open(localUrl, 'r') as file:
        fileContents = file.read()

    return {"message": fileContents}

@app.get("/txt/{ticker}{year}")
async def get_text(ticker, year ):
    '''GETS TEXT FROM HTML FILE'''
    return {"message": "some text"}

@app.get("/sentiment/{ticker}{year}")
async def get_sentiment(ticker, year ):
    '''gets the sentiments analysis'''
    return {"message": "some sentiment"}
