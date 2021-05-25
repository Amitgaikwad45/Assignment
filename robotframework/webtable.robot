#count no of rows ,columns, get data of the table
*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}      http://testautomationpractice.blogspot.com/
${browser}      chrome


*** Test Cases ***
WebTableImplementation
    open browser    ${url}  ${browser}
    maximize browser window
    #count no of rows and columns in a table
    ${rows}=    get element count    xpath://table[@name="BookTable"]/tbody/tr
    ${col}=     get element count    xpath://table[@name="BookTable"]/tbody/tr[1]/th

    log to console    ${rows}
    log to console    ${col}

    #retrieve specific element from the table
    ${data}=    get text    xpath://table[@name="BookTable"]/tbody/tr[5]/td[1]
    log to console    ${data}


    #validations on the table
    #specify the xpath of row and column no and name
    table column should contain    xpath://table[@name="BookTable"]     2   Author
    table row should contain        xpath://table[@name="BookTable"]    4   Learn JS
    table cell should contain       xpath://table[@name="BookTable"]    5   2   Mukesh
    table header should contain    xpath://table[@name="BookTable"]     BookName
    close window
*** Keywords ***
