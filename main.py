import argparse
from pathlib import Path
import os
import shutil


from html_redirect_file_generator import utilities

def setup_CLI() -> list:
    parser = argparse.ArgumentParser()

    parser.add_argument("data_path")
    parser.add_argument("generated_files_output_path")
    args = parser.parse_args()

    return args

def main():
    args = setup_CLI()

    os.mkdir(args.generated_files_output_path)

    repository_URL_and_path_pairs_list = utilities.get_repository_URL_and_path_pairs(args.data_path)
    leaf_ID_directories_list = utilities.get_leaf_ID_directories_list(repository_URL_and_path_pairs_list)
    utilities.generate_html_redirect_files_for_every_file_in_leaf_ID_directories(
                                                                leaf_ID_directory_dict_list= leaf_ID_directories_list,
                                                                output_generated_files_directory_path=args.generated_files_output_path)


if __name__ == '__main__':
    main()
