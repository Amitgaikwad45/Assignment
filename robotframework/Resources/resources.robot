*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
#creating userdefined keyword launchBrowser with arguments
launchBrowser
    [Arguments]    ${appurl}    ${appbrowser}
    open browser    ${appurl}  ${appbrowser}
    maximize browser window
    ${title}=   get title
    [Return]    ${title}
