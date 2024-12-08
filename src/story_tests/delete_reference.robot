*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Reference can be deleted from the main page
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
    Click Button    Delete
    Handle Alert
    Page Should Not Contain    Allan Collins and John Seely Brown and Ann Holum, Cognitive apprenticeship: making thinking visible, American Educator, 1991
    Deleting A Reference Should Succeed With Message    Successfully deleted reference Cognitive apprenticeship: making thinking visible

Server should ignore GET requests to deletion endpoint
    Go To Main Page
    Go To    http://${SERVER}/delete/invalid_id
    Main Page Should Be Open

Nothing happens if reference does not exist
    Go To Main Page
    Execute Javascript  (function() {const form = document.createElement('form'); form.method = 'post'; form.action='/delete/invalid_id';document.body.appendChild(form);form.submit(); }());
    Deleting A Non-Existent Reference Should Fail With Message    The reference could not be deleted.

*** Keywords ***
Deleting A Reference Should Succeed With Message
    [Arguments]  ${message}
    Main Page Should Be Open
    Page Should Contain  ${message}

Deleting A Non-Existent Reference Should Fail With Message
    [Arguments]  ${message}
    Main Page Should Be Open
    Page Should Contain  ${message}