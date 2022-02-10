'''
Author: Albert Tran
Created: 2020-08-08

Module for taking raw 10-k report data and cleaning html tags.


Example - Cleaning EDGAR html
-----------------------------
edgar_html = <text string containing 10-k html>
clean_html_text(edgar_html)

Example - Bulk Cleaning
-----------------------
>>> input_folder  = <path to edgar html files>
>>> output_folder = <path to where clean edgar files are written>
>>> write_clean_html_text_files(input_folder, output_folder)

'''

# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import os
import re
import string
# pylint: disable=E0401
from bs4 import BeautifulSoup


# %%
# ------------------------------------------------------------------------------
# HTML Cleaning
# ------------------------------------------------------------------------------
def __remove_special_characters(text):
    text = re.sub(r'[^\d\w\s' + string.punctuation + r']', r'', text)
    text = re.sub(r'\n{2,}', r'\n\n', text)
    return text


def clean_html_text(html_text):
    '''FUNCTION THAT CLEANS AN HTML FILE TO MORE READABLE TEXT'''
    clean_text = BeautifulSoup(html_text).get_text()
    clean_text = __remove_special_characters(clean_text)
    return clean_text


def get_10k_file_metadata(file_path):
    '''
    Gets metadata from filename.
    Input file is expected to be in the following format:
        <ticker>_10-k_<filing_date>.<extension>
    If file is not in the correct format, None is returned.
    Otherwise a tuple containing the ticker, report type and filing date are
    returned.
    '''
    # Check if the file is in the correct format
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    file_bits = file_name.split('_')
    if len(file_bits) != 3:
        return None

    # Return the metadata for the file
    ticker, report_type, filing_date = file_bits
    return (ticker, report_type, filing_date.split('.')[0])


def write_clean_html_text_files(input_folder, output_folder):
    '''WRITES CLEANED FILE TO A FOLDER'''
    # pylint: disable=C0301
    html_files = [f for f in os.listdir(input_folder) if (get_10k_file_metadata(f) and f.endswith('.html'))]

    for html_file in html_files:
        # Open file and extract text
        # pylint: disable=C0103
        with open(os.path.join(input_folder, html_file), 'r', encoding='utf-8') as f:
            html_text = f.read()
        clean_text = clean_html_text(html_text)

        # Write cleaned text
        file_name_out = os.path.splitext(os.path.basename(html_file))[0] + '.txt'
        file_path_out = os.path.join(output_folder, file_name_out)
        # pylint: disable=C0103
        with open(file_path_out, 'x', encoding='utf-8') as f:
            f.write(clean_text)
            print('File written: ', file_path_out)
