import unittest
from pathlib import Path
import os
import shutil

import operator # Used to sort lists of dicts
# import logging


from html_redirect_file_generator import utilities


# Get the test path
directory_path_of_this_test_file = Path(__file__).parent.resolve()

input_data_path: str = f'{directory_path_of_this_test_file}/tests_data'
output_generated_files_directory_path: str = f'{directory_path_of_this_test_file}/_generated'

class TestUtilities(unittest.TestCase):
    def test_format_git_repository_URL_to_https_00(self):
        input_URL = b'git@git.rwth-aachen.de:sebastian.neumeier/html-redirect-file-generator.git\n'
        target_output_URL = 'https://git.rwth-aachen.de/sebastian.neumeier/html-redirect-file-generator'

        # Test the function for correct output.
        self.assertEqual(target_output_URL, utilities.format_git_repository_URL_to_https(input_URL))

    def test_format_git_repository_URL_to_https_01(self):
        input_URL = b'git@git.rwth-aachen.de:fst-tuda/projects/designing-with-fluids/hydropulser/fst_asam_xil_api_matlab.git\n'
        target_output_URL = 'https://git.rwth-aachen.de/fst-tuda/projects/designing-with-fluids/hydropulser/fst_asam_xil_api_matlab'

        # Test the function for correct output.
        self.assertEqual(target_output_URL, utilities.format_git_repository_URL_to_https(input_URL))

    def test_format_git_repository_URL_to_https_02(self):
        input_URL = b'https://git.rwth-aachen.de/fst-tuda/projects/designing-with-fluids/hydropulser/fst_asam_xil_api_matlab.git\n'
        target_output_URL = 'https://git.rwth-aachen.de/fst-tuda/projects/designing-with-fluids/hydropulser/fst_asam_xil_api_matlab'

        # Test the function for correct output.
        self.assertEqual(target_output_URL, utilities.format_git_repository_URL_to_https(input_URL))

    def test_format_git_repository_URL_to_https_03(self):
        input_URL = b'ftp://test.test.de/test/test\n'

        # Test the function for correct output.
        with self.assertRaises(ValueError):
            utilities.format_git_repository_URL_to_https(input_URL)

    def test_format_git_repository_URL_to_https_04(self):
        # Test for URLs wit a token like the ones from GitLab
        input_URL = b'https://gitlab-ci-token:[MASKED]@git.rwth-aachen.de/sebastian.neumeier/html-redirect-file-generator.git\n'
        target_output_URL = 'https://git.rwth-aachen.de/sebastian.neumeier/html-redirect-file-generator'

        # Test the function for correct output.
        self.assertEqual(target_output_URL, utilities.format_git_repository_URL_to_https(input_URL))

    def test_format_git_repository_URL_to_https_05(self):
        # Test for git-URLs wit a token like the ones from GitLab
        input_URL = b'git@gitlab-ci-token:[MASKED]@git.rwth-aachen.de/sebastian.neumeier/html-redirect-file-generator.git\n'
        target_output_URL = 'https://git.rwth-aachen.de/sebastian.neumeier/html-redirect-file-generator'

        # Test the function for correct output.
        self.assertEqual(target_output_URL, utilities.format_git_repository_URL_to_https(input_URL))


class Test_check_if_string_is_UUID(unittest.TestCase):
    def test_00(self):
        UUID_string = '0184ebd9-988b-7bba-83e4-e24d90bf1352'

        # Test the function for correct output.
        self.assertTrue(utilities.check_if_string_is_UUID(UUID_string))

    def test_01(self):
        UUID_string = '1ed6c963-669f-62b7-8af6-3727686f020d'

        # Test the function for correct output.
        self.assertTrue(utilities.check_if_string_is_UUID(UUID_string))

    def test_02(self):
        # Wrong quantity of hex decimal digits in the last block
        wrong_UUID_string = '0184ebd9-988b-7bba-83e4-90bf1352'

        # Test the function for correct output.
        self.assertFalse(utilities.check_if_string_is_UUID(wrong_UUID_string))

    def test_03(self):
        # Wrong quantity of hex decimal blocks
        wrong_UUID_string = '0184ebd9-988b-7bba83e4-90bf1352'

        # Test the function for correct output.
        self.assertFalse(utilities.check_if_string_is_UUID(wrong_UUID_string))



class Test_search_for_hidden_git_directories(unittest.TestCase):
    def test_00(self):
        input_data_path: [str, path] = Path(f'{directory_path_of_this_test_file}/tests_data').resolve()

        target_output_hidden_git_directories_list__paths = [f'{directory_path_of_this_test_file}/tests_data/data_set_01_data_repository_html_redirect_file_generator/',
                                                            f'{directory_path_of_this_test_file}/tests_data/data_set_02_data_repository_html_redirect_file_generator/',
                                                            f'{directory_path_of_this_test_file}/tests_data/data_set_02_data_repository_html_redirect_file_generator/sensor/data_subset_manufacturer_03_data_repository_html_redirect_file_generator/']

        output_hidden_git_directories_list = utilities.search_for_hidden_git_directories(input_data_path)

        output_hidden_git_directories_list__paths = []
        for item in output_hidden_git_directories_list:
            output_hidden_git_directories_list__paths.append(item[0])

        self.assertEqual(target_output_hidden_git_directories_list__paths.sort(), output_hidden_git_directories_list__paths.sort())

class Test_get_repository_URL_and_path_pairs(unittest.TestCase):
    maxDiff = None

    def test_00(self):
        input_data_path: str = f'{directory_path_of_this_test_file}/tests_data/data_set_00'

        target_output_URL_path_pairs_list = [
            {
            'repository_URL': 'https://git.rwth-aachen.de/fst-tuda/public/html-redirect-file-generator/html-redirect-file-generator',
            'path': input_data_path
            }
        ]

        output_URL_path_pairs_list = utilities.get_repository_URL_and_path_pairs(input_data_path=input_data_path)
        self.assertEqual(target_output_URL_path_pairs_list, output_URL_path_pairs_list)

    def test_01(self):
        target_output_URL_path_pairs_list = [
            {
                'repository_URL': 'https://git.rwth-aachen.de/fst-tuda/public/html-redirect-file-generator/html-redirect-file-generator',
                'path': input_data_path
            },
            {
                'repository_URL': 'https://git.rwth-aachen.de/fst-tuda/public/html-redirect-file-generator/data_set_02_data_repository_html_redirect_file_generator',
                'path': f'{input_data_path}/data_set_02_data_repository_html_redirect_file_generator'
            },
            {
                'repository_URL': 'https://git.rwth-aachen.de/fst-tuda/public/html-redirect-file-generator/data_subset_manufacturer_03_data_repository_html_redirect_file_generator',
                'path': f'{input_data_path}/data_set_02_data_repository_html_redirect_file_generator/sensor/data_subset_manufacturer_03_data_repository_html_redirect_file_generator'
            },
            {
                'repository_URL': 'https://git.rwth-aachen.de/fst-tuda/public/html-redirect-file-generator/data_set_01_data_repository_html_redirect_file_generator',
                'path': f'{input_data_path}/data_set_01_data_repository_html_redirect_file_generator'
            }
        ]

        output_URL_path_pairs_list = utilities.get_repository_URL_and_path_pairs(input_data_path=input_data_path)
        self.assertEqual(target_output_URL_path_pairs_list.sort(key=operator.itemgetter('repository_URL')), output_URL_path_pairs_list.sort(key=operator.itemgetter('repository_URL')))



class Test_get_leaf_ID_directories_list(unittest.TestCase):
    def test_00(self):
        """ Check number of ID folders"""
        TARGET_NUMBER_ID_DIRECTORIES = 21

        input_data_path: str = f'{directory_path_of_this_test_file}/tests_data'

        repository_URL_and_path_pairs_list = utilities.get_repository_URL_and_path_pairs(input_data_path)
        leaf_ID_directories_list = utilities.get_leaf_ID_directories_list(repository_URL_and_path_pairs_list)

        self.assertEqual(TARGET_NUMBER_ID_DIRECTORIES, len(leaf_ID_directories_list))
        # self.assertEqual(['test'], leaf_ID_directories_list)

class Test__generate_html_redirect_files_for_every_file_in_leaf_ID_directory(unittest.TestCase):
    example_tuple = (
    '/home/sebastian/Desktop/html-redirect-file-generator/tests/tests_data/data_set_00/sensor/0184ebd9-988b-7bb9-a9f3-2a3cfc1631c3',
    [],
    ['rdf.ttl', 'README.md', 'rdf.json', 'rdf.xml']
    )

    leaf_ID_directory_dict_item = {'item_tuple': example_tuple,
                                   'repository_URL': 'https://git.rwth-aachen.de/sebastian.neumeier/html-redirect-file-generator'

    }

    target_files_list = ['0184ebd9-988b-7bb9-a9f3-2a3cfc1631c3.html',
                         '0184ebd9-988b-7bb9-a9f3-2a3cfc1631c3.ttl.html',
                         '0184ebd9-988b-7bb9-a9f3-2a3cfc1631c3.json.html',
                         '0184ebd9-988b-7bb9-a9f3-2a3cfc1631c3.xml.html',
                         '0184ebd9-988b-7bb9-a9f3-2a3cfc1631c3.md.html'
    ]

    output_generated_files_directory_path_olID_test = f'{output_generated_files_directory_path}_one_leaf_ID_directory_test'

    def test_00(self):
        """ Test if all .html file get generated"""
        # Setup create the _generated directory OR if present delete it and create
        try:
            os.mkdir(self.output_generated_files_directory_path_olID_test)
        except FileExistsError:
            shutil.rmtree(self.output_generated_files_directory_path_olID_test)
            os.mkdir(self.output_generated_files_directory_path_olID_test)

        utilities._generate_html_redirect_files_for_every_file_in_leaf_ID_directory(self.leaf_ID_directory_dict_item, self.output_generated_files_directory_path_olID_test)

        # There should be 5 generated files (see self.target_files_list)
        self.assertEqual(self.target_files_list.sort(), os.listdir(self.output_generated_files_directory_path_olID_test).sort())

    def test_01(self):
        """ Check if the .html files contain the correct redirect URL"""
        repository_URL = f'https://git.rwth-aachen.de/sebastian.neumeier/html-redirect-file-generator'
        repository_file_path = 'tests/tests_data/data_set_00/sensor/0184ebd9-988b-7bb9-a9f3-2a3cfc1631c3'
        for file_name in self.target_files_list:
            with Path(f'{self.output_generated_files_directory_path_olID_test}/{file_name}').open('r') as f:
                for line in f:
                    if 'meta' in line:
                        # Split the url out
                        url: str = line.split('url=')[-1].replace('" />\n', '')
                        file_name_suffixes = file_name.split('.')
                        if len(file_name_suffixes) == 2:
                            target_URL = f'{repository_URL}/-/tree/main/{repository_file_path}'
                        elif len(file_name_suffixes) == 3:
                            if file_name_suffixes[-2] == 'md':
                                target_URL = f'{repository_URL}/-/raw/main/{repository_file_path}/README.{file_name_suffixes[-2]}'
                            else:
                                target_URL = f'{repository_URL}/-/raw/main/{repository_file_path}/rdf.{file_name_suffixes[-2]}'
                        else:
                            raise Exception

                        self.assertEqual(target_URL, url)


class Test_generate_html_redirect_files_for_every_file_in_leaf_ID_directories(unittest.TestCase):
    output_generated_files_directory_path_fdd_test = f'{output_generated_files_directory_path}_full_data_directory_test'

    def test_00(self):
        """ Test generate all .html pages"""
        # Setup create the _generated directory OR if present delete it and create
        try:
            os.mkdir(self.output_generated_files_directory_path_fdd_test)
        except FileExistsError:
            shutil.rmtree(self.output_generated_files_directory_path_fdd_test)
            os.mkdir(self.output_generated_files_directory_path_fdd_test)


        repository_URL_and_path_pairs_list = utilities.get_repository_URL_and_path_pairs(input_data_path)
        leaf_ID_directory_dict_list = utilities.get_leaf_ID_directories_list(repository_URL_and_path_pairs_list)
        utilities.generate_html_redirect_files_for_every_file_in_leaf_ID_directories(leaf_ID_directory_dict_list,
                                                                                      self.output_generated_files_directory_path_fdd_test)

    def test_01(self):
        """ Check number of generated .html files"""
        html_files_per_ID_directory = 5
        target_number_generated_html_files = 21 * html_files_per_ID_directory

        self.assertEqual(target_number_generated_html_files, len(os.listdir(self.output_generated_files_directory_path_fdd_test)))
