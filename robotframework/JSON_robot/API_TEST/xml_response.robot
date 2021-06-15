*** Settings ***
Library    XML
Library    os
Library    Collections
Library    RequestsLibrary




*** Variables ***
${url}  http://thomas-bayer.com



*** Test Cases ***
SampleTest
    create session    mysession     ${url}
    ${response}     get request    mysession    /sqlrest/CUSTOMER/15
    ${xml_string}   convert to string    ${response.content}
    ${xml_obj}  parse xml    ${xml_string}

    #check single element value
    element text should be    ${xml_obj}  15        .//ID


    #check multiple values
    ${child_elements}   get child elements      ${xml_obj}
    should not be empty    ${child_elements}

    ${id}   get element text    ${child_elements[0]}
    should be equal    ${id}    15