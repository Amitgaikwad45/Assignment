#put method used to update data
*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  http://thetestingworldapi.com/



*** Test Cases ***
create new resource
    Create Session    AddData   ${url}
    ${body}     create dictionary   id=28  first_name=Testing     middle_name=ABCD87753   last_name=World     date_of_birth=12/12/1990
    ${header}   create dictionary    Content-Type=application/json
    ${response}     put request    AddData     /api/studentsDetails/28    data=${body}    headers=${header}
    log to console    ${response.status_code}
    log to console    ${response.content}
    ${response1}    get request    AddData      /api/studentsDetails/28
    log to console    ${response1.content}