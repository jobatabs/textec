*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Adding a valid reference
    Go To Main Page
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Submit New Reference
    Adding A Valid Reference Should Succeed With Message  Successfully added reference Cognitive apprenticeship: making thinking visible.

Adding a reference with invalid year
    Go To Main Page
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  nineteen ninety-one
    Submit New Reference
    Adding An Invalid Reference Should Fail With Message  Adding was unsuccessful. Invalid year.

Adding a reference with invalid pages pertinent
    Go To Main Page
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Set Pages Pertinent    kaksi
    Submit New Reference
    Adding An Invalid Reference Should Fail With Message  Invalid pages pertinent

Adding a reference with invalid pages pertinent format
    Go To Main Page
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Set Pages Pertinent    215-kolme
    Submit New Reference
    Adding An Invalid Reference Should Fail With Message  Invalid pages pertinent

Adding a reference with invalid pages pertinent format
    Go To Main Page
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Set Pages Pertinent    kolme-215
    Submit New Reference
    Adding An Invalid Reference Should Fail With Message  Invalid pages pertinent

*** Keywords ***
Adding A Valid Reference Should Succeed With Message
    [Arguments]  ${message}
    Main Page Should Be Open
    Page Should Contain  ${message}

Adding An Invalid Reference Should Fail With Message
    [Arguments]  ${message}
    Add Reference Page Should Be Open
    Page Should Contain  ${message}
