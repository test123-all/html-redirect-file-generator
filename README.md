# HTML-Redirect-File-Generator

## Introduction:
This is the repository of the HTML-Redirect-File-Generatorr  that generates simple html redirect files for data repositories to be able to redirect a whole persistent identifier (P_ID) namespace (for example https://w3id.org/fst/resource/ID) to a complex nested data repository structure. For more information about the P_ID redirecting service W3ID please have a look at https://w3id.org/ <br>

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

<b>DISCLAIMER:</b> <br>
This software is in a early proof of concept phase and mentioned in the ... paper. If you want to pay credit to this software in its current raw proof of concept state please cite the paper. <br>
<br>
Since this software is in a early proof of concept phase it is not commented out sufficiently yet, the functional segregation isn't good and in conclusion the function and variable names might be subject to siginificant change in the future. Therefore the backwards compatbility of the API won't be granted for now. <br>
<br>
As of the current plans the refactoring work will be done somewhere between the beginning of september 2024 and the end of december 2024 since the responsible person is a research aide and currently in exam phase. Thank you very much in advance for your understanding. <br>

## Current Maintainers:
sebastian.neumeieratstud.tu-darmstadt.de
