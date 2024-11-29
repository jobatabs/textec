*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.5 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${BROWSER}    chrome
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    ${prefs}  Create Dictionary
    ...  download.default_directory=.
    Call Method    ${options}  add_experimental_option  prefs  ${prefs}
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Reset References
    Go To  ${RESET_URL}

Go To Main Page
    Go To  ${HOME_URL}

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

Set Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Set Number
    [Arguments]  ${number}
    Input Text  number  ${number}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  id=publisher  ${publisher}

Set Howpublished
    [Arguments]  ${howpublished}
    Input Text  howpublished  ${howpublished}

Set Note
    [Arguments]  ${note}
    Input Text  note  ${note}


Set Pages Pertinent
    [Arguments]  ${pp}
    Input Text  pp  ${pp}

Submit New Reference
    Click Button  Save

Main Page Should Be Open
    Page Should Contain  Welcome to TexTec!

Add Reference Page Should Be Open
    Title Should Be  Add reference

Click Dropdown
    [Arguments]    ${dropdown_name}
    Click Element    name=${dropdown_name}

Select Type
    [Arguments]    ${dropdown_name}    ${value}
    Select From List By Value    name=${dropdown_name}    ${value}
