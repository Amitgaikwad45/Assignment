*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections
Library  SeleniumLibrary

*** Variables ***

${url}  https://jsonplaceholder.typicode.com/

*** Test Cases ***
BasicAuthenticate
    ${auth}     create list     5      229
    Create Session    mysession     ${url}  auth=${auth}
    #sending request to server
    ${response}     get request    mysession    /photos
    log to console      ${response.content}
    should be equal as strings    ${response.status_code}   200