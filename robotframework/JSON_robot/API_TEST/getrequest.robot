*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections



*** Variables ***
${url}      http://thetestingworldapi.com/
${browser}      chrome
${student_ID}   28

*** Test Cases ***
SampleTest
    create session    FetchData     ${url}
    ${response}     get request    FetchData    api/studentsDetails/${student_ID}
    ${actual_code}      convert to string    ${response.status_code}
    should be equal    ${actual_code}   200
    log to console    ${response.content}
    ${json_res}     to json    ${response.content}
    @{first_name_list}    get value from json   ${json_res}     data.first_name
    ${first_name}   get from list    ${first_name_list}     0
    log to console    ${first_name}
    should be equal    ${first_name}    Test Student
