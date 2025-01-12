<!-- heading declaration and main RDFa data declaration in HTML-->
<div xmlns:schema="https://schema.org/" typeof="schema:SoftwareSourceCode" id="software-1">
    <h1 property="schema:name">HTML-Redirect-File-Generator</h1>
    <meta property="schema:codeRepository" content="https://github.com/test123-all/html-redirect-file-generator">
    <meta property="schema:codeSampleType" content="full solution">
    <meta property="schema:license" content="https://opensource.org/licenses/MIT">
    <meta property="schema:programmingLanguage" content="Python">
    <h2>Introduction:</h2>
    <p property="schema:description">
        This is the repository of the HTML-Redirect-File-Generator that generates simple html redirect files for data
        repositories to be able to redirect a whole persistent identifier (p_ID) namespace (for example, 
        <a href="https://w3id.org/fst/resource/ID" target="_blank">https://w3id.org/fst/resource/ID</a>) to a complex
        nested data repository structure. For more information about the p_ID redirecting service W3ID please have a 
        look at 
        <a href="https://w3id.org/" target="_blank">https://w3id.org/</a> . <br>
        For more information about how this software is used in a p_ID redirecting service infrastructure please refer
        to the following paper:
        <ol>
            <li>
                <div>
                    <strong>
                        <span property="schema:name">How to Make Bespoke Experiments FAIR: Modular Dynamic Semantic Digital Twin and Open Source Information Infrastructure</span>
                        <span>(</span>
                        <a property="schema:relatedLink" href="https://preprints.inggrid.org/repository/view/40/" typeof="schema:Article"> 
                            <span>https://preprints.inggrid.org/repository/view/40/</span>
                        </a>
                        <span>)</span>
                    </strong>
                    <span>(January 2025, currently only available as a preprint.)</span>
                </div>
          </li>
        </ol>
    </p>
</div>


<b>DISCLAIMER:</b> <br>
This software in its current version is in an early proof of concept phase and directly used, mentioned and explained in the 
https://preprints.inggrid.org/repository/view/40/ paper. This first raw work in progress version was used to achieve the
results mentioned in the paper.<br>
<br>
Since this software is in an early proof of concept phase it is not commented out comprehensively yet,
the functional segregation isn't good and in conclusion the function and variable names might be subject to 
significant change in the future. Therefore, the backwards compatibility of the API won't be granted for now. <br>
<br>
Please note that we are no longer able to provide an exact time span for the refactoring work at this time, as the 
German government has recently reduced funding for scientific purposes overall, leaving the future of all sciences 
somewhat uncertain. Thank you very much for your understanding.


## How to use:
The `main.py` file provides a simple CLI Interface to the Python package:
```shell
usage: python3 main.py [-h] data_path generated_files_output_path

positional arguments:
data_path
generated_files_output_path

options:
-h, --help            show this help message and exit
```
TODO: Add an example with the GitLab CI/CD runner on how this package is used in combination with it.

## Possible Improvements:
The following list includes possible improvements that have been identified up to this version:
1. TODO: Extensive documentation beside the paper how the redirects work and why someone wants or needs to use them. -> What added value provides this python package?
2. TODO: Setup documentation of the software stack in an existing GitLab CI/CD runner environment.
3. TODO: Search for additional possible use cases and functions followed by a reevaluation of the current software 
structure and extensive refactoring of the existing code (add docstrings to the refactored functions, test case clean up and documentation).
4. TODO: function: Automatic checking of the repository structure.
5. TODO: function: Automatic checking of the RDF datasets again SHACL-profiles to validate the data structure and data semantic of the datasets.
6. Extend the support for other CI/CD web page ready software developer platforms. For example GitHub, Bitbucket, Gitea.
7. CI/CD test pipeline of this package on GitHub.
8. Sphinx documentation generator, through CI/CD of this package.



<!-- maintainer- and creator- RDFa data declaration in HTML-->
<div xmlns:schema="https://schema.org/" about="#software-1">
    <h2>Current Maintainer[s]:</h2>
    <div typeof="schema:Person">
        <strong property="schema:givenName">Sebastian</strong>
        <strong property="schema:familyName">Neumeier</strong>
        <strong>(<a href="https://orcid.org/0000-0001-9533-9004" property="schema:identifier">https://orcid.org/0000-0001-9533-9004</a>)</strong>
        <span property="schema:email">sebastian.neumeieratstud.tu-darmstadt.de</span>
    </div>
    <h2>Authors:</h2>
    <p xmlns:dcterms="http://purl.org/dc/terms/">The first running version of this software was originally created in 
         <span property="dcterms:date" content="2023-04-01">April 2023</span> 
         and 
         <span property="dcterms:date" content="2023-05-01">May 2023</span> 
     by:
    </p>
    <div typeof="schema:Person">
        <strong property="schema:givenName">Sebastian</strong>
        <strong property="schema:familyName">Neumeier</strong>
        <strong>(<a href="https://orcid.org/0000-0001-9533-9004" property="schema:identifier">https://orcid.org/0000-0001-9533-9004</a>)</strong>
        , <span property="schema:affiliation">
            Chair of Fluid Systems at Technical University of Darmstadt 
            (<a href="https://ror.org/05n911h24">https://ror.org/05n911h24</a>)
        </span>
        : <span property="schema:role">Conceptualization, Implementation, Documentation</span>.
    </div>
    <div typeof="schema:Person">
        <strong property="schema:givenName">Nils</strong>
        <strong property="schema:familyName">Preuß</strong>
        <strong>(<a href="https://orcid.org/0000-0002-6793-8533" property="schema:identifier">https://orcid.org/0000-0002-6793-8533</a>)</strong>
        , <span property="schema:affiliation">
            Chair of Fluid Systems at Technical University of Darmstadt 
            (<a href="https://ror.org/05n911h24">https://ror.org/05n911h24</a>)
        </span>
        : <span property="schema:role">Project Manager, Provider of the first raw idea of a better 
        redirect service and its requirements and constraints</span>.
    </div>
    <div typeof="schema:Person">
        <strong property="schema:givenName">Martin</strong>
        <strong property="schema:familyName">Hock</strong>
        <strong>(<a href="https://orcid.org/0000-0001-9917-3152" property="schema:identifier">https://orcid.org/0000-0001-9917-3152</a>)</strong>
        , <span property="schema:affiliation">
            Chair of Fluid Systems at Technical University of Darmstadt 
            (<a href="https://ror.org/05n911h24">https://ror.org/05n911h24</a>)
        </span>
        : <span property="schema:role">Support for the GitLab CI/CD Pipeline Technology</span>.
        <span property="schema:affiliation" resource="https://www.exampleinstitute.edu">Example Institute of Technology</span>
    </div>
    <div typeof="schema:Person">
        <strong property="schema:givenName">Manuel</strong>
        <strong property="schema:familyName">Rexer</strong>
        <strong>(<a href="https://orcid.org/0000-0003-0559-1156" property="schema:identifier">https://orcid.org/0000-0003-0559-1156</a>)</strong>
        , <span property="schema:affiliation">
            Chair of Fluid Systems at Technical University of Darmstadt 
            (<a href="https://ror.org/05n911h24">https://ror.org/05n911h24</a>)
        </span>
        : <span property="schema:role">Provider of Use Cases and Data Sets</span>.
    </div>
</div>
