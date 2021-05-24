#handling dropdowns and listboxes
*** Settings ***
Library  SeleniumLibrary



*** Variables ***
${browser}  chrome
${url}  https://www.techlistic.com/p/selenium-practice-form.html

*** Test Cases ***
Testing Radio Buttons and Check Boxes
    open browser    ${url}  ${browser}
    maximize browser window
    select from list by label    continents     Australia
    sleep    5
    select from list by index    continents     2
    sleep    5
    select from list by label    continents     South America

    #listboxes
    select from list by label    selenium_commands      Switch Commands
    select from list by label    selenium_commands      WebElement Commands
    sleep    3
    unselect from list by label    selenium_commands    Switch Commands

*** Keywords ***
