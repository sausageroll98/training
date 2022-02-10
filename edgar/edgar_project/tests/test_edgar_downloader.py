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

from edgar.edgar_downloader import *


# %%
# ------------------------------------------------------------------------------
# Unit Tests
# ------------------------------------------------------------------------------
# ***
# Tests - get_10k_filing_links
def test_get10_artifacts_aapl_2019():
    assert len(get_10k_artifact_links('AAPL', params={'dateb':r'2019/08/01'})) == 27

def test_get10_artifacts_aapl_2018():
    assert len(get_10k_artifact_links('AAPL', params={'dateb':r'2018/08/01'})) == 26

def test_get10_artifacts_msft_2015():
    assert len(get_10k_artifact_links('MSFT', params={'dateb':r'2015/01/01'})) == 21




# ***
# Checking links on artifact landing page are correct
def check_10k_doc_info(url_10k_artifacts_page, filing_date, accepted_date, 
    period_date, url, url_text):
    info = get_10k_doc_links(url_10k_artifacts_page)
    assert info['filing_date']   == filing_date
    assert info['accepted_date'] == accepted_date
    assert info['period_date']   == period_date
    assert info['url_html']      == url
    assert info['url_txt']       == url_text

# MSFT 1994
def test_10_doc_info_msft_1994():
    check_10k_doc_info(r'https://www.sec.gov/Archives/edgar/data/789019/0000891020-94-000175-index.html',
        '1994-09-27', '1994-09-27 00:00:00', '1994-06-30', None,
        r'https://sec.gov/Archives/edgar/data/789019/0000891020-94-000175.txt')

# MSFT 2004
def test_10_doc_info_msft_2004():
    check_10k_doc_info(r'https://www.sec.gov/Archives/edgar/data/789019/000119312504150689/0001193125-04-150689-index.htm',
        '2004-09-01', '2004-09-01 17:03:00', '2004-06-30',
        r'https://sec.gov/Archives/edgar/data/789019/000119312504150689/d10k.htm',
        r'https://sec.gov/Archives/edgar/data/789019/000119312504150689/0001193125-04-150689.txt')

# AAPL 1998
def test_10_doc_info_aapl_1998():
    check_10k_doc_info(r'https://www.sec.gov/Archives/edgar/data/320193/0001047469-98-044981-index.html',
        '1998-12-23', '1998-12-23 00:00:00', '1998-09-25', None,
        r'https://sec.gov/Archives/edgar/data/320193/0001047469-98-044981.txt')

# AAPL 2008
def test_10_doc_info_aapl_2008():
    check_10k_doc_info(r'https://www.sec.gov/Archives/edgar/data/320193/000119312508224958/0001193125-08-224958-index.htm',
        '2008-11-05', '2008-11-05 06:16:23', '2008-09-27', 
        r'https://sec.gov/Archives/edgar/data/320193/000119312508224958/d10k.htm',
        r'https://sec.gov/Archives/edgar/data/320193/000119312508224958/0001193125-08-224958.txt')

# AAPL 2018
def test_10_doc_info_aapl_2018():
    check_10k_doc_info(r'https://www.sec.gov/Archives/edgar/data/320193/000032019318000145/0000320193-18-000145-index.htm',
        '2018-11-05', '2018-11-05 08:01:40', '2018-09-29', 
        r'https://sec.gov/Archives/edgar/data/320193/000032019318000145/a10-k20189292018.htm',
        r'https://sec.gov/Archives/edgar/data/320193/000032019318000145/0000320193-18-000145.txt')

# CVX 1995
def test_10_doc_info_cvx_1995():
    check_10k_doc_info(r'https://www.sec.gov/Archives/edgar/data/93410/0000093410-95-000012-index.html',
        '1995-03-30', '1995-03-30 00:00:00', '1994-12-31', None,
        r'https://sec.gov/Archives/edgar/data/93410/0000093410-95-000012.txt')

# CVX 2005
def test_10_doc_info_cvx_2005():
    check_10k_doc_info(r'https://www.sec.gov/Archives/edgar/data/93410/000095013405004137/0000950134-05-004137-index.htm',
        '2005-03-03', '2005-03-03 08:36:36', '2004-12-31', 
        r'https://sec.gov/Archives/edgar/data/93410/000095013405004137/f04196e10vk.htm',
        r'https://sec.gov/Archives/edgar/data/93410/000095013405004137/0000950134-05-004137.txt')

# CVX 2015
def test_10_doc_info_cvx_2015():
    check_10k_doc_info(r'https://www.sec.gov/Archives/edgar/data/93410/000009341015000010/0000093410-15-000010-index.htm',
        '2015-02-20', '2015-02-20 11:36:43', '2014-12-31', 
        r'https://sec.gov/Archives/edgar/data/93410/000009341015000010/cvx-123114x10kdoc.htm',
        r'https://sec.gov/Archives/edgar/data/93410/000009341015000010/0000093410-15-000010.txt')



# ***
# Checking file writing capabilities
def test_write_page(tmpdir):
    file_path = tmpdir.join('output.htm')
    url = r'https://www.sec.gov/Archives/edgar/data/789019/000119312504150689/d10k.htm'
    write_page(url, file_path)
    assert file_path.read().strip().endswith(r'</DOCUMENT>')


def test_download_files_10k():
    # TODO: Write tests here.
    pass

