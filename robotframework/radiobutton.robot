*** Settings ***
Library  SeleniumLibrary



*** Variables ***
${browser}  chrome
${url}  https://www.techlistic.com/p/selenium-practice-form.html

*** Test Cases ***
Testing Radio Buttons and Check Boxes
    open browser    ${url}  ${browser}
    maximize browser window
    #every statement waits for 2 seconds
    set selenium speed    2seconds
    #selecting radio buttons pass name of the radio button and value
    select radio button     sex     Female
    select radio button    exp  1

    #checkboxes
    select checkbox    Manual Tester
    select checkbox    Automation Tester
    unselect checkbox    Manual Tester

*** Keywords ***
