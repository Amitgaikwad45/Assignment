#grouping tests

*** Settings ***



*** Test Cases ***
TC1
    [Tags]    regression
    log to console    This is user reg test
    log to console    reg test is over

TC2
    [Tags]    sanity
    log to console    This is login test
    log to console    login test is over

TC3
    [Tags]    regression
    log to console    change in user setting
    log to console    changes done

TC4
    [Tags]    sanity
    log to console    This is logout test
    log to console    logout test is over



