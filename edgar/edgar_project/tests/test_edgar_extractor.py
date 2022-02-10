'''
Created: 2020-08-07
Author : Albert Tran

'''
# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import sys
sys.path.append('..')

import pytest
from edgar.edgar_extractor import *

# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
@pytest.fixture()
def resource_msft2020():
    url = r'https://www.sec.gov/Archives/edgar/data/789019/000156459020034944/msft-10k_20200630.htm'
    yield Filing10K(requests.get(url).text)

@pytest.fixture()
def resource_aapl_2019():
    url = r'https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/a10-k20199282019.htm'
    yield Filing10K(requests.get(url).text)

@pytest.fixture()
def resource_cvx2018():
    url = r'https://www.sec.gov/Archives/edgar/data/93410/000009341018000010/cvx12312017-10kdoc.htm'
    yield Filing10K(requests.get(url).text)

@pytest.fixture()
def resource_jpm2010():
    url = r'https://www.sec.gov/Archives/edgar/data/19617/000095012310016029/e82150e10vk.htm'
    yield Filing10K(requests.get(url).text)


def test_toc_msft2020(resource_msft2020):
    print(resource_msft2020.toc)
    assert resource_msft2020.toc['Item1']  == 3
    assert resource_msft2020.toc['Item2']  == 32
    assert resource_msft2020.toc['Item7']  == 35
    assert resource_msft2020.toc['Item7a'] == 54

def test_toc_aapl_2019(resource_aapl_2019):
    assert resource_aapl_2019.toc['Item1']  == 1
    assert resource_aapl_2019.toc['Item2']  == 14
    assert resource_aapl_2019.toc['Item7']  == 18
    assert resource_aapl_2019.toc['Item7a'] == 26

def test_toc_cvx2018(resource_cvx2018):
    assert resource_cvx2018.toc['Item1']  == 3
    assert resource_cvx2018.toc['Item2']  == 22
    assert resource_cvx2018.toc['Item7']  == 24
    assert resource_cvx2018.toc['Item7a'] == 24

def test_toc_jpm2010(resource_jpm2010):
    # Strange corner case where the pages are of the format 246-250 instead of
    # just a single number
    assert resource_jpm2010.toc['Item1']  == 1
    assert resource_jpm2010.toc['Item2']  == 10
    assert resource_jpm2010.toc['Item7']  == 19
    assert resource_jpm2010.toc['Item7a'] == 19

def test_mda_text_msft2020(resource_msft2020):
    assert resource_msft2020.extract_mda_text()[:20]  == 'PART II\nItem 7\n\xa0\nITE'
    assert resource_msft2020.extract_mda_text()[-20:] == '\n\nEarnings\n\n\xa0\n\xa0\n\xa0\n54'

def test_mda_text_aapl_2019(resource_aapl_2019):
    assert resource_aapl_2019.extract_mda_text()[:20]  == '\n\nItem 7.Management’'
    assert resource_aapl_2019.extract_mda_text()[-20:] == ' 2019 Form 10-K | 26'

def test_mda_text_cvx2018(resource_cvx2018):
    assert resource_cvx2018.extract_mda_text()[:20]  == '\n\nPART\xa0II\n\nItem 5. M'
    assert resource_cvx2018.extract_mda_text()[-20:] == 'Disclosure\nNone.\n\n24'

@pytest.mark.xfail(reason="Logic to find page numbers does not work for the JP Morgan report.")
def test_mda_text_jpm2010(resource_jpm2010):
    # Finding page numbers does not work on JP Morgan's reports!
    assert resource_jpm2010.extract_mda_text()[:20]  == 'This test is broken'
    assert resource_jpm2010.extract_mda_text()[-20:] == 'This test is broken'








'''


url_msft_2020 = r'https://www.sec.gov/Archives/edgar/data/19617/000095012310016029/e82150e10vk.htm'
response = requests.get(url_msft_2020)
msft_2020_10k = Filing10K(response.text)

msft_2020_10k.toc
msft_2020_10k.extract_mda_text()[:20]
msft_2020_10k.extract_mda_text()[-20:]


url_msft_2020 = r'https://www.sec.gov/Archives/edgar/data/789019/000156459020034944/msft-10k_20200630.htm'
response = requests.get(url_msft_2020)
msft_2020_10k = Filing10K(response.text)

msft_2020_10k.extract_mda_text()[:20]
msft_2020_10k.extract_mda_text()[-20:]


url = r'https://www.sec.gov/Archives/edgar/data/19617/000095012310016029/e82150e10vk.htm'
blah = Filing10K(requests.get(url).text)
blah.toc

import re

regex = re.compile(r'\d+')
blah = regex.findall('11-23...666')
dir(blah)
blah.groups()


# ***
# Management Information
url_msft_2020 = r'https://www.sec.gov/Archives/edgar/data/789019/000156459020034944/msft-10k_20200630.htm'
response = requests.get(url_msft_2020)
msft_2020_10k = Filing10K(response.text)

msft_2020_10k.toc
msft_2020_10k.extract_mda_text()




msft_2020_10k.write_mda_text(os.path.join(data_dir, 'md_msft_2020.txt'))



write_management_info(response.text, os.path.join(data_dir, 'md_msft_2020.txt'))

url_aapl_2019 = r'https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/a10-k20199282019.htm'
response = requests.get(url_aapl_2019)
write_management_info(response.text, os.path.join(data_dir, 'md_aapl_2020.txt'))

url_cvx_2018 = r'https://www.sec.gov/Archives/edgar/data/93410/000009341018000010/cvx12312017-10kdoc.htm'
response = requests.get(url_cvx_2018)
write_management_info(response.text, os.path.join(data_dir, 'md_cvx_2018.txt'))

minfo = get_management_info(response.text)


from bs4 import BeautifulSoup

url = r'https://www.sec.gov/Archives/edgar/data/19617/000095012310016029/e82150e10vk.htm'
requests.get(url).text
BeautifulSoup()

Filing10K(requests.get(url))

jpm2010_10k = resource_jpm2010()
jpm2010_10k.toc




data_dir = r'D:\temp\junk\10k_reports'


# ***
# Management Information
url_msft_2020 = r'https://www.sec.gov/Archives/edgar/data/789019/000156459020034944/msft-10k_20200630.htm'
response = requests.get(url_msft_2020)
msft_2020_10k = Filing10K(response.text)

msft_2020_10k.toc
msft_2020_10k.extract_mda_text()




msft_2020_10k.write_mda_text(os.path.join(data_dir, 'md_msft_2020.txt'))



write_management_info(response.text, os.path.join(data_dir, 'md_msft_2020.txt'))

url_aapl_2019 = r'https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/a10-k20199282019.htm'
response = requests.get(url_aapl_2019)
write_management_info(response.text, os.path.join(data_dir, 'md_aapl_2020.txt'))

url_cvx_2018 = r'https://www.sec.gov/Archives/edgar/data/93410/000009341018000010/cvx12312017-10kdoc.htm'
response = requests.get(url_cvx_2018)
write_management_info(response.text, os.path.join(data_dir, 'md_cvx_2018.txt'))

minfo = get_management_info(response.text)

'''