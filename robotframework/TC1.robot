*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/




*** Test Cases ***
#<<Title of testcase>>
LoginTest

    open browser    ${url}  ${browser}
    loginToApplication
    close browser


*** keywords ***
loginToApplication

    click link  xpath://a[@class='ico-login']
    input text  id:Email    ag33826@gmail.com
    input text  id:Password     Amit@123
    click element   xpath://button[@class='button-1 login-button' and text()='Log in']



