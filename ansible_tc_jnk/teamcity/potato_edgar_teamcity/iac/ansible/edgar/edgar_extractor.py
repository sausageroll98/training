# pylint: disable=C0303
# pylint: disable=C0301
# pylint: disable=C0116
# pylint: disable=W0631
'''
Author : Albert Tran
Created: 2020-08-07

Module for extracting sections from a 10-k filing report in html format.
'''
# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import re

# pylint: disable=W0611
import requests

# pylint: disable=E0401
from bs4 import BeautifulSoup

# pylint: disable=C0411
import warnings
warnings.warn("the spam module is deprecated", DeprecationWarning,
              stacklevel=2)


# %%
# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------
# pylint: disable=C0115
class Filing10K:
    def __init__(self, html_text):
        self.soup = BeautifulSoup(html_text)
        self.toc  = self.get_table_of_contents_dict()


    @staticmethod
    def __is_table_of_contents(tag):
        # Grab the table info as text, and remove special characters
        table_text = tag.get_text().lower()
        table_text = re.sub(r'[^a-zA-Z0-9 ]', r'', table_text)

        # Check whether the main items are in the table of contents
        has_item1  = 'business' in table_text
        has_item1a = 'risk factors' in table_text
        has_item1b = 'unresolved staff comments' in table_text
        has_item2  = 'properties' in table_text
        has_item3  = 'legal proceedings' in table_text
        has_item4  = 'mine safety disclosures' in table_text

        has_item5 = 'market for registrants common equity' in table_text
        has_item6 = 'selected financial data' in table_text
        has_item7 = 'managements discussion and analysis' in table_text
        has_item8 = 'quantitative and qualitative disclosures about market risk' in table_text
        has_item9 = 'financial statements and supplementary data' in table_text

        # Return True if most of the contents are available
        item_flags = [has_item1, has_item1a, has_item1b, has_item2, has_item3, 
                      has_item4, has_item5, has_item6, has_item7, has_item8, has_item9]
        return (sum(item_flags)/len(item_flags)) > 0.7

    # pylint: disable=R1710
    def __get_table_of_contents_soup(self):
        table_list = self.soup.find_all('table')
        for table in table_list:
            if self.__is_table_of_contents(table):
                return table
        print('Unable to find table of contents.')


    def get_table_of_contents_dict(self):
        toc_soup = self.__get_table_of_contents_soup()
        if toc_soup is None:
            return None

        items = {'business':'Item1', 
                'risk factors':'Item1a', 
                'unresolved staff comments':'Item1b', 
                'properties':'Item2', 
                'legal proceedings':'Item3',
                'mine safety disclosures':'Item4', 
                'managements discussion and analysis of financial condition and results of operations':'Item7',
                'quantitative and qualitative disclosures about market risk':'Item7a',
                'financial statement and supplementary data':'Item8'}
        toc_dict = {}
        for row in self.soup.find_all('tr'):
            curr_context = None
            for row_item in row.find_all('td'):
                cell_contents = row_item.get_text().lower().strip() 
                clean_cell_contents = re.sub(r'[^a-zA-Z0-9 ]', '', cell_contents)

                # pylint: disable=C0201
                if clean_cell_contents in items.keys():
                    curr_context = clean_cell_contents
                matches = re.compile(r'\d+').findall(cell_contents)
                if curr_context and matches and cell_contents.startswith(matches[0]):
                    toc_dict[items[curr_context]] = int(matches[0])
        return toc_dict


    @staticmethod
    def get_page_number(break_tag):
        '''
        Given a break, return the page number after the break.
        '''
        try:
            prev_tag = break_tag.find_previous_sibling().get_text().strip()
            page_tag = prev_tag.replace('|', ' ').split(' ')
            page_num = int([number for number in page_tag if number.isnumeric()][-1]) + 1
            return page_num # The page number after the break
        # pylint: disable=W0702
        except:
            return None


    def extract_pages(self, start_page, end_page):
        '''
        Extracts pages in the filing from the start page up to (and including)
        the end page.
        '''
        # Find all breaks (used to get page numbers)
        soup_breaks = self.soup.find_all('hr')

        # Navigate to the start page
        for curr_tag in soup_breaks:
            if self.get_page_number(curr_tag) == start_page:
                break

        # Go through the html from the start page until the end page
        text_list = []
        while curr_tag.find_next_sibling():
            curr_tag = curr_tag.find_next_sibling()
            if curr_tag.name == 'hr':
                page_num = self.get_page_number(curr_tag)
                if page_num > end_page:
                    break
            text_list.append(curr_tag.get_text())

        return_text = '\n'.join(text_list)
        return_text = re.sub(r'\s+\n{2,}', r'\n\n', return_text)
        return return_text


    def extract_mda_text(self):
        # Figure out where the management discussion and analysis starts/ends
        start_page = self.toc['Item7']
        end_page   = self.toc['Item7a']

        # Get the text between the pages
        mi_text = self.extract_pages(start_page, end_page)
        return mi_text


    def write_mda_text(self, output_file):
        mda_text = self.extract_mda_text()
        # pylint: disable=W1514
        # pylint: disable=C0103
        with open(output_file, 'x') as f:
            f.write(mda_text)

# %%
