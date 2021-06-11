*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections



*** Variables ***
${url}      http://thetestingworldapi.com/
${browser}      chrome




*** Test Cases ***
Sample Test
    create session     AddData      ${url}
    &{body}     create dictionary    first_name=Testing     middle_name=A   last_name=world     date of birth=12/12/1990
    &{header}   create dictionary    Content-Type=application/json
    ${response}     post request       AddData  /api/studentsDetails    data=${body}    headers=${header}
    ${code}     convert to string    ${response.status_code}
    should be equal    ${code}  201
