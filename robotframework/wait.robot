#sleep selenium speed selenium timeout implicit wait
*** Settings ***
Library  SeleniumLibrary



*** Test Cases ***
RegTest
    #default selenium speed
    #${speed}=   get selenium speed
    #log to console    ${speed}
    open browser    http://demowebshop.tricentis.com/register   chrome
    maximize browser window
    #${time}=    get selenium timeout
    #log to console    ${time}

    #set selenium timeout    10 seconds
    #wait until page contains    Registeration       #wait for 5 seconds which is default timeout

    #set selenium speed    2 seconds     #every statement work with 2 seconds delay
    ${implicittime}=    get selenium implicit wait
    log to console    ${implicittime}
    set selenium implicit wait    10 seconds
    ${implicittime}=    get selenium implicit wait  #gives 10 seconds
    log to console    ${implicittime}


    select radio button     Gender     M
    input text  name:FirstName1      John
    input text  name:LastName       Kenedy
    input text  name:Email      abc@gmail.com
    input text  name:Password   John123
    input text  name:ConfirmPassword    John123

    #${speed}=   get selenium speed
    #log to console    ${speed}
    #close all browsers

