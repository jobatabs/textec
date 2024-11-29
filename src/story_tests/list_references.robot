*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Unsuccessfully saved reference is not listed on main page
    Go To Main Page
    Click Dropdown  type
    Select Type  type  article
    Click Button  Go
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  nineteen ninety-one
    Submit New Reference
    Go To Main Page
    Page Should Not Contain  Allan Collins and John Seely Brown and Ann Holum, Cognitive apprenticeship: making thinking visible, American Educator, 1991

Successfully saved reference is listed on main page
    Go To Main Page
    Click Dropdown  type
    Select Type  type  article
    Click Button  Go
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Submit New Reference
    Page Should Contain  Allan Collins and John Seely Brown and Ann Holum, Cognitive apprenticeship: making thinking visible, American Educator, 1991