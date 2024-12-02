*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Editing an added reference
    Go To Main Page
    Click Dropdown    type
    Select Type    type    article
    Click Button    Go
    Set Author  Allan Collins and John Seely Brown and Ann Holum
    Set Title  Cognitive apprenticeship: making thinking visible
    Set Journal  American Educator
    Set Year  1991
    Set Volume  50
    Set Number  2
    Submit New Reference
    Go To Main Page
    Click Button    Edit
    Set Author  Rune Klevjer
    Set Title  In defense of cutscenes
    Set Journal  Computer games and digital culture conference proceedings
    Set Year  2002
    Set Volume  50
    Set Number  2
    Save Edited Reference
    Editing A Valid Reference Should Succeed With Message    Rune Klevjer, In defense of cutscenes, Computer games and digital culture conference proceedings, 50, 2, 2002


*** Keywords ***
Editing A Valid Reference Should Succeed With Message
    [Arguments]  ${message}
    Main Page Should Be Open
    Page Should Contain  ${message}