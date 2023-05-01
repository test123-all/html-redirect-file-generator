import unittest
from pathlib import Path
import os
from time import sleep

import requests
from bs4 import BeautifulSoup

# Get the test path
directory_path_of_this_test_file = Path('__file__').parent.resolve()

output_generated_files_directory_path: str = f'{directory_path_of_this_test_file}/_generated'
output_generated_files_directory_path_for_all_files = f'{output_generated_files_directory_path}_all'

# class TestHtmlResolvability(unittest.TestCase):
#     def test_00(self):
#         html_files_list = os.listdir(output_generated_files_directory_path_for_all_files)
#
#         for file_name in html_files_list:
#             url = f'http://192.168.101.114:5251/{file_name}'
#             response = requests.get(url, allow_redirects=True)
#
#             MAX_HTML_REDIRECT_COUNT = 5
#             html_redirect_counter = 0
#             while response.headers['Content-Type'] == 'text/html':
#                     soup = BeautifulSoup(response.content, 'html.parser')
#                     meta_http_equiv_refresh_soup = soup.findAll('meta', 'http-equiv'=="refresh")
#                     # No redirect in html
#                     if len(meta_http_equiv_refresh_soup) == 0:
#                         raise Exception
#                     # More than one redirect in the .html, should never occur because the html reference forbids it
#                     elif len(meta_http_equiv_refresh_soup) > 1:
#                         raise Exception
#
#                     redirect_URL = meta_http_equiv_refresh_soup[0]['content'].split('url=')[-1]
#
#                     response = requests.get(redirect_URL, allow_redirects=True)
#
#                     html_redirect_counter = +1
#                     if html_redirect_counter >= MAX_HTML_REDIRECT_COUNT:
#                         print(Warning(f'The maximum amount of html redirects (={MAX_HTML_REDIRECT_COUNT}) is reached,'
#                                       f' there is a problem with the start URL:{url}'))
#                         break
#
#             print(response.text)
#             self.assertEqual(response.status_code, 200)
#             sleep(1) # second