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
    Enter email                 xyz@example.com
    #Switch tab
    Enter password              John@123


Fetch user
    Get username

Fetch Options
    Fetch all options

Tms Section
    Enter Tms section

Title
    Enter title         raise ticket


Description
    Enter description    software

Raise ticketoption
    Enter Raiseticket

History
    Enter History

#LogoutTest
 #   Enter logout btn
