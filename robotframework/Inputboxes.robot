*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/





*** Test Cases ***
TestingInputBox
    open browser    ${url}  ${browser}
    maximize browser window
    title should be     nopCommerce demo store
    click link  xpath://a[@class='ico-login']
#store email id in email_txt variable
    ${"email_txt"}  set variable    id:Email
#check element email_txt visible or not
    element should be visible   ${"email_txt"}
    element should be enabled   ${"email_txt"}
    #element should be visible   ${"email_txt"} test gets fail

    input text      ${"email_txt"}   ag33826@gmail.com
    sleep   5
    clear element text  ${"email_txt"}
    close browser


*** Keywords ***
