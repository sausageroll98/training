# pylint: disable=C0114
# pylint: disable=W0612
## THIS FILE IS INCOMPLETE, THE FUNCTIONS DO NOT YET WORK AND SHOUD NOT BE USED

# pylint: disable=C0103
# pylint: disable=C0304
# pylint: disable=R1710
def checkYearValidity(year):
    '''NONSENCE'''
    if year < 2000 or year > 2021:
        return {"ERROR": f"year {year} is invalid"}

# pylint: disable=C0304
def getFileName(ticker, year, html_files):
    '''NONSENCE'''
    inFolder = False
    for i in html_files:
        if ticker in i and str(year) in i:
            inFolder = True
            fileName = i
