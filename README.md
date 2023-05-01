# data_repository_site_generator
## Introduction:
This is the repository of the data_repository_site_generator that generates simple html redirect files for data repositories to be able to redirect a whole persistent identifier (P_ID) namespace (for example https://w3id.org/fst/resource/ID) to a complex nested data repository structure. For more information about the P_ID redirecting service W3ID please have a look at https://w3id.org/ <br>

TODO: Add a documentation how the redirects work and why someone wants or needs to use it. -> What added value provides this python package? <br>

The `main.py` file provides a simple CLI Interface to the Python package:
```shell
usage: python3 main.py [-h] data_path generated_files_output_path

positional arguments:
data_path
generated_files_output_path

options:
-h, --help            show this help message and exit
```

**Please Note:** <br>
1. The package name is still work in progess and might be a subject to change.
2. The package is a first minimal working example and the code is not documented properly and the code still needs to be refactored.

## Current Maintainers:
nils.preussatfst.tu-darmstadt.de
martin.hockatfst.tu-darmstadt.de
sebastian.neumeieratstud.tu-darmstadt.de
