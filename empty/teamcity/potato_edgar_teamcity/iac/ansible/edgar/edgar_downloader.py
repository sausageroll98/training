'''
Created: 2020-08-03
Author : Albert Tran

Module to download 10-k reports from the SEC via EDGAR.
https://www.sec.gov/edgar/searchedgar/companysearch.html

# Neat trick!
# With EDGAR data, make sure that the right html pages are scraped, not the ones with JS.
https://stackoverflow.com/questions/61234991/python-automatic-table-scraping-from-complex-html

# Unicode ascii stuff
https://stackoverflow.com/questions/40872126/python-replace-non-ascii-character-in-string

# Sentiment analysis stuff
https://sraf.nd.edu/textual-analysis/resources/
https://www.uts.edu.au/sites/default/files/ADG_Cons2015_Loughran%20McDonald%20JE%202011.pdf

# Example 10-k forms
AAPL 2019 https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/a10-k20199282019.htm
AAPL 2009 https://www.sec.gov/Archives/edgar/data/320193/000119312508224958/d10k.htm
MSFT 2020 https://www.sec.gov/Archives/edgar/data/789019/000156459020034944/msft-10k_20200630.htm
CVX  2019 https://www.sec.gov/Archives/edgar/data/93410/000009341020000010/cvx12312019-10kdoc.htm
GS   2019 https://www.sec.gov/Archives/edgar/data/886982/000119312520043853/d826673d10k.htm

Random notes:
Some years don't have the report in a nice html format.
Sometimes text can be in span tags (AAPL), div tags (GS) or p tags (MSFT).

'''
# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import os
import re
#pylint: disable =import-error
import requests
#pylint: disable =import-error
from bs4 import BeautifulSoup



# %%
# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

def get_10k_artifact_links(symbol, params=None):
    '''
    Arguments
    ---------
    symbol: The ticker symbol for the listed company.
    params: A dictionary containing additional query parameters for the search.

    Returns
    -------
    Returns a list of links. Each link will correspond to one submission and
    will contain all links to all artifacts for that submission.

    '''
    # Setting up the query string parameters
    count       = 100 # TODO: Automatically page  # pylint: disable=fixme
    report_type = '10-k'
    q_params    = {'action':'getcompany', 'CIK':symbol,
                   'count':count, 'type':report_type, 'output':'atom'}
    headers = {'User-Agent':'Admin admin@gmail.com'}
    if isinstance(params, dict):
        q_params.update(params)

    # Getting the 10k links
    url_endpoint = r'https://www.sec.gov/cgi-bin/browse-edgar'
    response     = requests.get(url_endpoint, q_params, headers=headers)

    # Getting all filing page links for each filing
    soup         = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    if 'Request Rate Threshold Exceeded' in str(soup):
        raise Exception("Request Rate Exceeded")

    filing_pages = [link_tag['href'] for link_tag in soup.find_all('link') \
                    if '-index.htm' in link_tag['href']]
    return filing_pages


# 2. Getting the link for the filing data
#pylint: disable =too-many-locals
#pylint: disable =unused-argument
def get_10k_doc_links(filing_page_html, prefix=''):
    '''
    Given a filing page with all filing artifacts, return links to the 10-k
    in text and html formats, as well as some other relevant information.

    Arguments
    ---------
    filing_page_html: A url for a page containing all artifacts for a given filing.

    Returns
    -------
    A dictionary containing:
    - filing_date: The date of the submission
    - url        : The html link to the actual 10-k report
    - url_txt    : The html link to the actual 10-k report as text

    Examples
    --------

    '''
    # Download the page html
    headers = {'User-Agent':'Admin admin@gmail.com'}
    response = requests.get(filing_page_html, headers=headers)
    soup     = BeautifulSoup(response.text, 'html.parser')

    # Get the filing date
    form_soup = soup.find('div', {'class':'formContent'}).find_all('div', {'class':'infoHead'})
    for item in form_soup:
        if item.text.strip() == 'Filing Date':
            filing_date = item.find_next_sibling('div').text
        elif item.text.strip() == 'Accepted':
            accepted_date = item.find_next_sibling('div').text
        elif item.text.strip() == 'Period of Report':
            period_date = item.find_next_sibling('div').text


    # Get the table that contains all the documents in the filing
    soup = soup.find_all('table', {'summary':'Document Format Files'})[0]

    # Look at the table headers
    headers    = [header.text for header in soup.find_all('th')]
    index_type = headers.index('Type')
    index_doc  = headers.index('Document')
    index_desc = headers.index('Description')

    # Look through each row until the 10-K artifact is found
    link_10k = None
    txt_10k  = None
    doc_type = None
    table_rows = soup.find_all('tr')
    #pylint: disable = unused-variable
    for i, row in enumerate(table_rows):
        row_items = row.find_all('td')
        if not row_items:
            continue
        row_type = row_items[index_type].text.strip().lower()
        row_doc  = row_items[index_doc].text.strip().lower()
        row_desc = row_items[index_desc].text.strip().lower()
        if (row_type.startswith('10-k')) and (row_doc != ''):
            doc_type = row_type
            link_10k = row_items[index_doc].find('a')['href']
            link_10k = r'https://sec.gov' + link_10k.replace(r'/ix?doc=', '')
        elif (row_desc == 'complete submission text file') and (row_doc != ''):
            txt_10k = row_items[index_doc].find('a')['href']
            txt_10k = r'https://sec.gov' + txt_10k

    # Return the URL
    return {'filing_date'  : filing_date,
            'accepted_date': accepted_date,
            'period_date'  : period_date,
            'doc_type'     : doc_type,
            'url_html'     : link_10k,
            'url_txt'      : txt_10k}


def write_page(url, file_path):
    '''Nothing to explain here'''
    headers = {'User-Agent':'Admin admin@gmail.com'}
    response = requests.get(url, headers=headers)
    #pylint: disable = no-else-return
    #pylint: disable = invalid-name
    if response.status_code != 200:
        print('Unable to retrieve content from: ', url)
        return
    else:
        with open(file_path, 'x', encoding='utf-8') as f:
            f.write(response.text)


def download_files_10k(ticker, dest_folder, year = "all"):
    '''
    Downloads 10-k files to directory.
    cNote that directory needs to already exist.
    '''
    filing_pages  = get_10k_artifact_links(ticker)
    info_list_10k = [get_10k_doc_links(page) for page in filing_pages]

    success = True
    response_text = ""
    loop_ender = False

    for info in info_list_10k:
        if year == "all" or year in info['filing_date']:
            loop_ender = True
            try:
                # Note that 10-k amendments are not included.
                doc_type  = re.sub(r'[/_]', '', info['doc_type'])
                file_name = ticker + '_' + doc_type + '_' + info['filing_date'] +'.html'
                if (info['url_html'] is not None) and (doc_type == '10-k') :
                    file_name = ticker + '_' + doc_type + '_' + info['filing_date'] +'.html'
                    file_path = os.path.join(dest_folder, file_name)
                    write_page(info['url_html'], file_path)
                    print('File write complete: ', file_name)
                    response_text += "Everything works"
                elif doc_type != '10-k':
                    print('Skipping file      : ', file_name)
                    response_text += f'Skipping file {file_name}'
            #pylint: disable = broad-except
            #pylint: disable = invalid-name
            except Exception as e:
                success = False
                filing_date = info['filing_date']
                if filing_date[0] == '1':
                    response_text += f'Error: Date {filing_date} is before 2000'
                else:
                    print(f'File write failed for {ticker} with filing date {filing_date}.')
                    print(e)
                    #pylint: disable = line-too-long
                    response_text += f"File write failed for {ticker} with filing date {filing_date}"
    #pylint: disable = singleton-comparison
    if loop_ender == False:
        success = False
        response_text = f'Could no locate 10-k for {ticker} for the queried year'
    return (success, response_text)
