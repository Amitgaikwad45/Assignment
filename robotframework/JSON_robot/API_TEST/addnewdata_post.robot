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
    #for put request we need to send body
    ${body}     create dictionary    first_name=Testing     middle_name=A   last_name=World     date_of_birth=12/12/1990
    ${header}   create dictionary    Content-Type=application/json
    ${response}     post request    AddData     /api/studentsDetails    data=${body}    header=${header}
    ${code}     convert to string    ${response.status_code}
    should be equal    ${code}  201
    log to console    ${response.content}