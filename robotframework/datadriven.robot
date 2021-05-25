*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/login_resources.robot
#executed once before actual testcases started
Suite Setup    open my browser
#after execution of all the tests all the browsers should be closed
Suite Teardown    close browsers
Test Template       Invalid login

*** Test Cases ***          username                password
Right user empty pass       admin@yourstore.com     ${EMPTY}
Right user wrong pass       admin@yourstore.com     xyz
Wrong user right pass       adm@yourstore.com       admin
Wrong user empty pass       adm@yourstore.com       ${EMPTY}
Wrong user wrong pass       adm@yourstore.com       xyz


*** Keywords ***
Invalid login
    [Arguments]    ${username}  ${password}
    Input username    ${username}
    Input pwd    ${password}
    click login button
    error message should be visible
