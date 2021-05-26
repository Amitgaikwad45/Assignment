*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/LoginKeywords.robot

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/index.php/auth/login
${browser}  chrome
${user}     Admin
${pwd}      admin123


*** Test Cases ***
LoginTest
#calling keywords defined from resource file by passing arguments
    open my browser    ${url}   ${browser}
    Enter Username    ${user}
    Enter Password    ${pwd}
    click login button
    sleep    3 seconds
    verify login
    close my browser