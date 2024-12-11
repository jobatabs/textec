*** Settings ***
Library  SeleniumLibrary
Library    XML

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.5 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${BROWSER}    chrome
${HEADLESS}   false
${BUTTON_LOCATOR}    xpath=//button[text()='Save']

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
    Clear Element Text    author
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Clear Element Text    title
    Input Text  title  ${title}

Set Journal
    [Arguments]  ${journal}
    Clear Element Text    journal
    Input Text  journal  ${journal}
 
Set Year
    [Arguments]  ${year}
    Clear Element Text    year
    Input Text  year  ${year}

Set Volume
    [Arguments]  ${volume}
    Clear Element Text    volume
    Input Text  volume  ${volume}

Set Number
    [Arguments]  ${number}
    Clear Element Text    number
    Input Text  number  ${number}

Set Publisher
    [Arguments]  ${publisher}
    Clear Element Text    id=publisher
    Input Text  id=publisher  ${publisher}

Set Howpublished
    [Arguments]  ${howpublished}
    Clear Element Text    howpublished
    Input Text  howpublished  ${howpublished}

Set Note
    [Arguments]  ${note}
    Clear Element Text    note
    Input Text  note  ${note}


Set Pages Pertinent
    [Arguments]  ${pp}
    Clear Element Text    pp
    Input Text  pp  ${pp}

Submit New Reference
    Scroll Element Into View    ${BUTTON_LOCATOR}
    Click Button  Save

Save Edited Reference
    Scroll Element Into View    ${BUTTON_LOCATOR}
    Click Button    Save

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
