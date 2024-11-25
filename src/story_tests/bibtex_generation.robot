*** Settings ***
Resource  resource.robot
Library  OperatingSystem
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References
Variables  vars.py

*** Test Cases ***
A BibTeX file can be downloaded
    [Teardown]  Remove Downloaded File
    Go To Main Page
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Submit New Reference
    Page Should Contain  Allan Collins and John Seely Brown and Ann Holum, Cognitive apprenticeship: making thinking visible, American Educator, 1991
    Click Button    Export BibTeX file
    ${bibfile}  Get File    ./references.bib
    Should Contain    ${bibfile}    ${COGNITIVE_APPRENTICESHIP_BIBTEX}


*** Keywords ***
Remove Downloaded File
  Remove File    ./references.bib