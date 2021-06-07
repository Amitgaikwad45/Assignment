*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/




*** Test Cases ***
#<<Title of testcase>>
#to run testcase separate robot -t LoginTest TestCases\TC1.robot
#robot -t LoginTest --settag==smoke TestCases\TC1.robot
#robot --include smoke TestCases\TC1.robot run testcases by tag name
#to run with more [tags]  robot -i smoke -i sanity TestCases\TC1.robot
#robot -i s* TestCases\TC1.robot executes all the testcases starting with letter s
LoginTest

    [Tags]    smoke
    open browser    ${url}  ${browser}
    click link  xpath://a[@class='ico-login']
    input text  id:Email    ag33826@gmail.com
    input text  id:Password     Amit@123
    click element   xpath://button[@class='button-1 login-button' and text()='Log in']
    close browser

SampleTest
    [Tags]    sanity
    log    Hello world
SecondTest
    log    I am in second test
    set tags    regression1



