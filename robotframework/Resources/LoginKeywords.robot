#keywords used in LoginTest_POM
*** Settings ***
Library     SeleniumLibrary
#specify file which contains locators
Variables    ../PageObjects/Locators.py

*** Keywords ***
Open my browser
    [Arguments]    ${url}    ${browser}
    open browser    ${url}  ${browser}
    maximize browser window

Enter Username
    [Arguments]    ${username}
    #locator refering from locators file
    input text    ${txt_loginUserName}      ${username}

Enter Password
    [Arguments]    ${password}
    #locator refering from locators file
    input text    ${txt_loginPassword}      ${password}

click login button
    click button    ${btn_login}

verify login
    #title should be      OrangeHRM
    element text should be    xpath://b[text()='Dashboard']     Dashboard

close my browser
    close all browsers
