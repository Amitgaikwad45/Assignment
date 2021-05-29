*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/robotass_keywords.robot

*** Variables ***
${url}      https://erp.afourtech.com/
${browser}  chrome


*** Test Cases ***
LoginTest
    Open my browser    ${url}   ${browser}
    click signin button
    Switch tab
    Enter email                 amit.gaikwad@afourtech.com
    #Switch tab
    Enter password              Amitgaikwad@123


Fetch user
    Get username

Fetch Options
    Fetch all options

Raise ticketoption
    Enter Raiseticket

Tms Section
    Enter Tms section
#LogoutTest
 #   Enter logout btn
