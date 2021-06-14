*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  http://thetestingworldapi.com/



*** Test Cases ***
validate delete request
    create session    Appaccess     ${url}
    ${response}     delete request      Appaccess       api/studentsDetails/28
    ${code}     convert to string    ${response.status_code}
    should be equal    ${code}  200
    ${jsonresponse}     to json    ${response.content}
    ${status_list}  get value from json     ${jsonresponse}     status
    ${status}   get from list   ${status_list}  0
    should be equal    ${status}    true