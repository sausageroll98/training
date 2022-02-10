from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI()

def main(ticker,year):
    data_dir = r'C:\ce02\temp\junk\10k_reports_raw'

    import sys
    sys.path.insert(0,".")

    import edgar_downloader as edgar_downloader
    import ref_data as edgar_refdata
    from tqdm import tqdm

    #df_sp100 = edgar_refdata.get_sp100()
    #tickers  = df_sp100['Symbol']

    #tickers  = ['MSFT', 'AAPL', 'CVX', 'FB', 'WMT'] 

    for i, tickers in enumerate(ticker):
        print(f'{((i+1)/len(ticker))*100}% complete. Current ticker: {tickers}.')
        edgar_downloader.download_files_10k(tickers, data_dir)
        print('--------------------------------')

    print('done')

@app.get("/")
async def root():
    return {"message": "Lets scrape a 10K"}

@app.get("/app/10k/{ticker}{year}")
async def main():
    return {"text": main("https://www.sec.gov/ix?doc=/Archives/edgar/data/320193/000032019321000105/aapl-20210925.htm")}