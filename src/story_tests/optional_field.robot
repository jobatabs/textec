*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Adding a valid reference without optional field
    Go To Main Page
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Submit New Reference
    Go To Main Page
    Page Should Contain  Allan Collins and John Seely Brown and Ann Holum, Cognitive apprenticeship: making thinking visible, American Educator, 1991

Adding a reference with optional field (multiple pages pertinent)
    Go To Main Page
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Set Pages Pertinent  213-250
    Submit New Reference
    Go To Main Page
    Page Should Contain  Allan Collins and John Seely Brown and Ann Holum, Cognitive apprenticeship: making thinking visible, American Educator (pp. 213-250), 1991

Adding a reference with optional field (single page pertinent)
    Go To Main Page
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Set Pages Pertinent  213
    Submit New Reference
    Go To Main Page
    Page Should Contain  Allan Collins and John Seely Brown and Ann Holum, Cognitive apprenticeship: making thinking visible, American Educator (pp. 213), 1991
