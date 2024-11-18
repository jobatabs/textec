*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Adding a valid reference
    Go To  ${HOME_URL}
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Submit New Reference
    Main Page Should Be Open
    Adding A Valid Reference Should Succeed With Message  Successfully added reference Cognitive apprenticeship: making thinking visible.

Adding a reference with invalid year
    Go To  ${HOME_URL}
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  nineteen ninety-one
    Submit New Reference
    Adding An Invalid Reference Should Fail With Message  Adding was unsuccessful. Invalid year.

Unsuccessfully saved reference is not listed on main page
    Go To  ${HOME_URL}
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  nineteen ninety-one
    Submit New Reference
    Go To  ${HOME_URL}
    Page Should Not Contain  Allan Collins and John Seely Brown and Ann Holum, Cognitive apprenticeship: making thinking visible, American Educator, 1991

Successfully saved reference is listed on main page
    Go To  ${HOME_URL}
    Click Link  Add a new reference
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Submit New Reference
    Page Should Contain  Allan Collins and John Seely Brown and Ann Holum, Cognitive apprenticeship: making thinking visible, American Educator, 1991

*** Keywords ***
Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}
 
Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Submit New Reference
    Click Button  Save

Adding A Valid Reference Should Succeed With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Adding An Invalid Reference Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Main Page Should Be Open
    Page Should Contain  Welcome to TexTec!