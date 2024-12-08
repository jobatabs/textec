*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Search Finds Relevant References
    Go To Main Page
    Click Dropdown  type
    Select Type  type  article
    Click Button  Go
    Set Author  Allan Collins
    Set Title  Cognitive apprenticeship
    Set Journal  American Educator
    Set Year  1991
    Submit New Reference
    Click Dropdown  type
    Select Type  type  book
    Click Button  Go
    Set Author  John Doe
    Set Title  Learning Python
    Set Publisher  O'Reilly
    Set Year  2020
    Submit New Reference
    Perform Search  Cognitive apprenticeship
    Page Should Contain  Allan Collins, Cognitive apprenticeship, American Educator, 1991
    Page Should Not Contain  John Doe, Learning Python, O'Reilly, 2020

Search Returns No Results For Nonexistent Reference
    Go To Main Page
    Perform Search  Nonexistent
    Page Should Contain  Sorry, we couldn't find any matches!

Search With Empty Query Redirects To Main Page
    Go To Main Page
    Go To    http://${SERVER}/result?query=
    Main Page Should Be Open

Search Is Case Insensitive
    Go To Main Page
    Click Dropdown  type
    Select Type  type  article
    Click Button  Go
    Set Author  Jane Smith
    Set Title  Case Insensitive Search
    Set Journal  Testing Journal
    Set Year  2023
    Submit New Reference
    Perform Search  case insensitive
    Page Should Contain  Jane Smith, Case Insensitive Search, Testing Journal, 2023

Search Finds References By Partial Input
    Go To Main Page

    Click Dropdown  type
    Select Type  type  article
    Click Button  Go
    Set Author  Author One
    Set Title  Title One
    Set Journal  Journal One
    Set Year  2022
    Submit New Reference

    Click Dropdown  type
    Select Type  type  article
    Click Button  Go
    Set Author  Author Two
    Set Title  Title Two
    Set Journal  Journal Two
    Set Year  2022
    Submit New Reference

    Click Dropdown  type
    Select Type  type  article
    Click Button  Go
    Set Author  Author Three
    Set Title  Title Three
    Set Journal  Journal Three
    Set Year  2021
    Submit New Reference

    Perform Search  22
    Page Should Contain  Author One, Title One, Journal One, 2022
    Page Should Contain  Author Two, Title Two, Journal Two, 2022
    Page Should Not Contain  Author Three, Title Three, Journal Three, 2021

*** Keywords ***
Perform Search
    [Arguments]  ${query}
    Go To Main Page
    Input Text  name=query  ${query}
    Click Button  xpath=//input[@type='submit']
