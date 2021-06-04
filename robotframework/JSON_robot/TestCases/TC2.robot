*** Settings ***
Library    ../PageObjects/locators.py
Library    SeleniumLibrary
Library    Collections


*** Variables ***
${browser}  chrome
${url}      http://www.thetestingworld.com/testings




*** Test Cases ***
Open url
      open browser        ${url}      ${browser}
      maximize browser window

Sample Testcase
    [Tags]  Smoke
    ${username}=    Read Element Locator    Registration.username_textbox
    input text    name:${username}  Testing

    ${password}=    Read Element Locator    Registration.password_textbox
    input text    name:fld_email    test@gmail.com
    input text    name:${password}  123456
    sleep    2s
    close window

*** Keywords ***
Read Element Locator
    [Arguments]    ${JsonPath}
    ${result}=  read_locator_from_json  ${JsonPath}

    [Return]    ${result}
