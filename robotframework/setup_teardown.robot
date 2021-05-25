*** Settings ***
Library    SeleniumLibrary

#executes once before suit is started
Suite Setup     log to console      Opening browser
#executed once after completion of test suite
Suite Teardown     log to console      Opening browser

#executes every time before starting of every testcase
Test Setup         log to console      logged in
#executes every time after completion of every testcase
Test Teardown     log to console      logged out

*** Test Cases ***
TC01
    log to console    This is prepaid recharge test
TC02
    log to console    This is postpaid recharge test
TC03
    log to console    This is search recharge test
TC04
    log to console    This is advsearch recharge test