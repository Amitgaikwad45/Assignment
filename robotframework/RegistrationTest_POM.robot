*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/RegistrationKeywords.robot

*** Variables ***
${url}      http://demowebshop.tricentis.com/register/
${browser}  chrome


*** Test Cases ***
RegistrationTest

    Open my browser     ${url}      ${browser}
    Select Gender
    Enter Firstname         John
    Enter Lastname          kenedy
    Enter Email             srqp22@gmail.com
    Enter Password          johnxyz
    Confirmpassword    johnxyz
    click register button
    verify registration
    close my browser
