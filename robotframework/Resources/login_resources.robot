#data driven testing datadriven.robot
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${Login_url}        https://admin-demo.nopcommerce.com
${browser}      chrome


*** Keywords ***
open my browser
    open browser    ${login_url}    ${browser}
    maximize browser window

close browsers
    close all browsers

open login page
    go to    ${login_url}

Input username
    [Arguments]    ${username}
    input text    id:Email      ${username}
Input pwd
    [Arguments]    ${password}
    input text    id:Password   ${password}

click login button
    click element    xpath://button[@class='button-1 login-button']

click logout link
    click link    Logout

#If login fails error message should be visible
Error message should be visible
    page should contain    Login was unsuccessful

#In case of successful login
Dashboard page should be visible
    page should contain    Dashboard