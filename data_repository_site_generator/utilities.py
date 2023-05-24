from pathlib import Path
import shutil
import os
import subprocess


def get_repository_URL_and_path_pairs(input_data_path: [str, Path]) -> list:
    list_of_hidden_git_directories = search_for_hidden_git_directories(input_data_path=input_data_path)

    # Get all the repository urls
    data_repository_URL_path_pairs_list = []
    sp = subprocess.run(['git', 'config', '--get', 'remote.origin.url'], capture_output=True, cwd=input_data_path)
    d = {
        'repository_URL': format_git_repository_URL_to_https(sp.stdout),
        'path': input_data_path
    }

    data_repository_URL_path_pairs_list.append(d)

    for hidden_git_directory_item in list_of_hidden_git_directories:
        sp = subprocess.run(['git', 'config', '--get', 'remote.origin.url'], capture_output=True, cwd=hidden_git_directory_item[0])
        d = {
            'repository_URL': format_git_repository_URL_to_https(sp.stdout),
            'path': hidden_git_directory_item[0]
        }

        data_repository_URL_path_pairs_list.append(d)

    return data_repository_URL_path_pairs_list

def search_for_hidden_git_directories(input_data_path: [str, Path]) -> list:
    walked_directories = os.walk(input_data_path)
    # Search for ".git" directories to identify git repositories
    list_of_hidden_git_directories = []
    for item in walked_directories:
        if '.git' in item[2]:
            list_of_hidden_git_directories.append(item)

    sp = subprocess.run(['git', 'status'], capture_output=True, cwd=input_data_path)
    if sp.stderr == b'fatal: not a git repository (or any of the parent directories): .git\n':
        raise FileNotFoundError("The given data path doesn't belong to a git repository!")

    if not list_of_hidden_git_directories:
        print(Warning(("WARNING: Not one connected repository submodule \".git\" directory could be found on the input_data_path directory tree. "
                       "Please double check if your data repositories are properly added as git submodules.")))

    return list_of_hidden_git_directories


def format_git_repository_URL_to_https(URL: bytes) -> str:
    decoded_URL = URL.decode('UTF-8')

    # Remove special characters
    # Decide wether it is a git or https URL
    # TODO: WARN: Since there are two functions that split on a @ this might cause serious problems! I don't have
    #             enough testcases at hand at the moment to test all possibilities thoroughly.
    if ('gitlab-ci-token' in decoded_URL
            and not 'git@' in decoded_URL):
        formatted_URL = decoded_URL.split('@')[-1]
        formatted_URL = formatted_URL.replace('\n', '')
        formatted_URL = formatted_URL.replace('.git', '')
        formatted_https_URL = f'https://{formatted_URL}'

    elif 'git@' in decoded_URL:
        formatted_URL = decoded_URL.split('@')[-1].replace(':', '/')
        formatted_URL = formatted_URL.replace('\n', '')
        formatted_URL = formatted_URL.replace('.git', '')
        formatted_https_URL = f'https://{formatted_URL}'

    elif 'https://' in decoded_URL:
        formatted_URL = decoded_URL.replace('\n', '')
        formatted_URL = formatted_URL.replace('.git', '')
        formatted_https_URL = formatted_URL
    else:
        raise ValueError("Expected a git repository URL as bytes string object like:\n"
                         "b'git@git.rwth-aachen.de:fst-tuda/projects/designing-with-fluids/hydropulser/fst_asam_xil_api_matlab.git\\n' or"
                         "b'https://git.rwth-aachen.de/fst-tuda/projects/designing-with-fluids/hydropulser/fst_asam_xil_api_matlab.git\\n' \n."
                         f"You provided:{URL}"
                         )

    return formatted_https_URL


def get_customized_html_template(url: str) -> str:
    # TODO: SECURITY: Add checks for the input since this functions ia a possible target for a code injection attack
    html_file_redirect_template: str = ('<!DOCTYPE html>\n'
                                        '<html>\n'
                                        '  <head>\n'
                                       f'    <meta http-equiv="refresh" content="0; url={url}" />\n'
                                        '  </head>\n'
                                        '  <body>\n'
                                        '  </body>\n'
                                        '</html>\n')

    return html_file_redirect_template


def check_if_string_is_UUID(input_string: str) -> bool:
    # 8-4-4-4-12
    seperated_string = input_string.split('-')

    if len(seperated_string) != 5:
        return False

    if not (    len(seperated_string[0]) == 8
                and len(seperated_string[1]) == 4
                and len(seperated_string[2]) == 4
                and len(seperated_string[3]) == 4
                and len(seperated_string[4]) == 12
            ):
        return False

    return True


def get_leaf_ID_directories_list(data_repository_URL_path_pairs_list: list) -> list:
    leaf_ID_directories_dict_list = []

    for _ in range(len(data_repository_URL_path_pairs_list)):
        data_repository_URL_path_pair = data_repository_URL_path_pairs_list.pop(0)

        remaining_paths_to_mine = []
        for item in data_repository_URL_path_pairs_list:
            remaining_paths_to_mine.append(item['path'])

        walked_directories = os.walk(data_repository_URL_path_pair['path'])

        for item in walked_directories:
            # If the path is part of a different repository continue
            # Woran merke ich, dass das Teil eines anderes Repositortires ist? -> wenn der aktuelle Pfad teil eines der anderen repository Pfade ist
            # TODO: nested geht damit aber nicht
            # Wenn einer von remaining_paths_to_mine in item vorhanden ist überspringe
            continueFlag: int = 0
            for remaining_path in remaining_paths_to_mine:
                if remaining_path in item[0]:
                    continueFlag = 1
                    break

            if continueFlag == 1:
                continue

            # If (the traversed directory doesn't have any subdirectories)
            #     AND the contained number of files is bigger than one (for example if there is only the README.md)
            if not item[1] and len(item[2]) > 1:
                leaf_ID_directories_dict_list.append({
                                                 'item_tuple': item,
                                                 'repository_URL': data_repository_URL_path_pair['repository_URL']
                                                }
                )

    return leaf_ID_directories_dict_list


def _generate_html_redirect_files_for_every_file_in_leaf_ID_directory(leaf_ID_directory_dict_item: dict, output_generated_files_directory_path: [str, Path]) -> None:
    SUPPORTED_RAW_FILE_EXTENSIONS = ['owl', 'ttl', 'json', 'xml', 'md']
    BRANCH_TAG: str = 'main'
    # create all necessary html files
    # 1ed6c963-669f-62b7-8af6-3727686f020d.html -> 'https://git.rwth-aachen.de/sebastian.neumeier/test_w3id_redirect/-/tree/main/1ed6c963-669f-62b7-8af6-3727686f020d'
    # 1ed6c963-669f-62b7-8af6-3727686f020d.ttl.html
    # 1ed6c963-669f-62b7-8af6-3727686f020d.json.html
    # 1ed6c963-669f-62b7-8af6-3727686f020d.xml.html
    # 1ed6c963-669f-62b7-8af6-3727686f020d.md.html
    file_name_prefix = leaf_ID_directory_dict_item['item_tuple'][0].split('/')[-1]

    # Create file for the repository ID redirect
    file_path: str = f'{output_generated_files_directory_path}/{file_name_prefix}.html'
    # Get the relative file path of the repository
    repository_name = leaf_ID_directory_dict_item['repository_URL'].split('/')[-1]
    relative_repository_path = leaf_ID_directory_dict_item['item_tuple'][0].split(f'{repository_name}/')[-1]
    file_url: str = f"{leaf_ID_directory_dict_item['repository_URL']}/-/tree/{BRANCH_TAG}/{relative_repository_path}"

    Path(file_path).touch()
    with Path(file_path).open('w') as f:
        f.write(get_customized_html_template(file_url))


    # Create files for the raw redirects
    for file_item in leaf_ID_directory_dict_item['item_tuple'][2]:
        file_name_suffix = file_item.split('.')[-1]
        if file_name_suffix in SUPPORTED_RAW_FILE_EXTENSIONS:
            file_path = f'{output_generated_files_directory_path}/{file_name_prefix}.{file_name_suffix}.html'
            repository_name = leaf_ID_directory_dict_item['repository_URL'].split('/')[-1]
            relative_repository_path = leaf_ID_directory_dict_item['item_tuple'][0].split(f'{repository_name}/')[-1]
            file_url = f"{leaf_ID_directory_dict_item['repository_URL']}/-/raw/{BRANCH_TAG}/{relative_repository_path}/{file_item}"

            Path(file_path).touch()
            with Path(file_path).open('w') as f:
                f.write(get_customized_html_template(file_url))
        else:
            continue


def generate_html_redirect_files_for_every_file_in_leaf_ID_directories(leaf_ID_directory_dict_list: list, output_generated_files_directory_path: [str, Path]) -> None:
    if len(os.listdir(Path(output_generated_files_directory_path).resolve())) != 0:
        raise FileExistsError(f'The given path: {output_generated_files_directory_path} \n'
                              ' where the to be generated .html files should be saved to, is not empty!\n')

    for leaf_ID_directory_dict_item in leaf_ID_directory_dict_list:
        _generate_html_redirect_files_for_every_file_in_leaf_ID_directory(leaf_ID_directory_dict_item,
                                                                         output_generated_files_directory_path)