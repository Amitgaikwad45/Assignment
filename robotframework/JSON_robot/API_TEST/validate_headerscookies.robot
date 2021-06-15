*** Settings ***
Library    XML
Library    os
Library    Collections
Library    RequestsLibrary




*** Variables ***
${url}  http://jsonplaceholder.typicode.com



*** Test Cases ***
TestHeaders
    create session    mysession     ${url}
    #creating request
    ${response}     get request    mysession    /photos

    #printing all the headers from the response(headers are in the form of keys and values)
    log to console    ${response.headers}
    #passing content type as a key and return value
    ${content_type_value}   get from dictionary    ${response.headers}      Content-Type
    should be equal     ${content_type_value}       application/json; charset=utf-8


    ${content_encode_value}   get from dictionary    ${response.headers}      Content-Encoding
    should be equal     ${content_encode_value}       gzip

TestCookies
    create session    mysession     ${url}
    #creating request
    ${response}     get request    mysession    /photos

    #displaying all the cookies from response
    #log to console      ${response.cookies}


    ${cookiesvalue}     get from dictionary    ${response.cookies}      __cfduid
    log to console    ${cookiesvalue}   #Display specific cookie value
