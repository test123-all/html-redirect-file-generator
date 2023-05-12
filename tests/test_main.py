import unittest
from pathlib import Path
import os
import shutil
import subprocess

# Get the test path
directory_path_of_this_test_file = Path('__file__').parent.resolve()

input_data_path: str = f'{directory_path_of_this_test_file}/tests_data'
print(input_data_path)
output_generated_files_directory_path: str = f'{directory_path_of_this_test_file}/_generated'

class TestCLI(unittest.TestCase):
    output_generated_files_directory_path_test_CLI = f'{output_generated_files_directory_path}_test_CLI'
    def test_00(self):
        # Setup delete the _generated directory if present
        if Path(self.output_generated_files_directory_path_test_CLI).exists():
            shutil.rmtree(self.output_generated_files_directory_path_test_CLI)

        cwd = os.getcwd()
        os.chdir(Path(f'{directory_path_of_this_test_file}/../').resolve())

        command_list = ['python3', f'{directory_path_of_this_test_file}/../main.py', input_data_path, self.output_generated_files_directory_path_test_CLI]
        try:
            sp = subprocess.run(command_list, capture_output=True, cwd=input_data_path)
            if sp.returncode != 0:
                raise Exception("Subprocess Error:\n"
                               f"{sp.stderr.decode('UTF-8')}")
        except Exception:
            os.chdir(cwd)
            raise

