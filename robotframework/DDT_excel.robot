#data driven testing using data driver package
*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/login_resources.robot
Library     DataDriver      ../TestData/LoginData.xlsx      sheet_name=Sheet1
#executed once before actual testcases started
Suite Setup    open my browser

#after execution of all the tests all the browsers should be closed
Suite Teardown    close browsers
#to execute multiple times
Test Template    Invalid login

*** Test Cases ***
#test case execution depends on input provided in excel file
LoginTestwithExcel using ${username}    ${password}


*** Keywords ***
#user defined keyword
Invalid login
    [Arguments]    ${username}  ${password}
    Input username    ${username}
    Input pwd    ${password}
    click login button
    error message should be visible
