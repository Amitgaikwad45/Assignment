*** Settings ***
Library     SeleniumLibrary
#specify file which contains locators
Variables    ../PageObjects/Locators.py

*** Keywords ***
Open my browser
    [Arguments]    ${url}    ${browser}
    open browser    ${url}  ${browser}
    maximize browser window
Select Gender
    select radio button    Gender      M


Enter Firstname
    [Arguments]    ${fname}
    #locator refering from locators file
    input text    ${txt_fnm}      ${fname}

Enter Lastname
    [Arguments]    ${lname}
    #locator refering from locators file
    input text    ${txt_lnm}      ${lname}

Enter Email
    [Arguments]    ${mail}
    #locator refering from locators file
    input text    ${txt_email}      ${mail}

Enter Password
    [Arguments]    ${pwd}
    #locator refering from locators file
    input text    ${txt_pwd}      ${pwd}

Confirmpassword
    [Arguments]    ${cpwd}
    #locator refering from locators file
    input text    ${txt_cpwd}      ${cpwd}


click register button
    click button    ${btn_reg}

verify registration
    #title should be      OrangeHRM
    page should contain    Your registration completed

close my browser
    close all browsers
