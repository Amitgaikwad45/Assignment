*** Settings ***
Library    SeleniumLibrary


*** Variables ***
@{ROBOTS}=        Bender    Johnny5    Terminator    Robocop


*** Test Cases ***
Forloop1
     FOR    ${robot}    IN    @{ROBOTS}
        Exit For Loop If    $robot == 'Johnny5'
        log to console    ${robot}
    END

Forloop2
    FOR    ${i}    IN RANGE    1      10
       exit for loop if    ${i} == 5
       log to console    ${i}

    END

Forwithlist
    @{items}    create list    11   22    33
    FOR    ${j}    IN    @{items}
      exit for loop if    $j == '33'
      log to console    ${j}
    END
