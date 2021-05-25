#userdefined keywords separated in resources.robot

*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/resources.robot
*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/index.php/auth/login/
${browser}      chrome
*** Test Cases ***
TC1
    #returning value
    ${page_title}=  launchBrowser   ${url}  ${browser}
    log to console    ${page_title}
    #diplay title to report
    log    ${page_title}
    input text    id:txtUsername    Admin
    input text    id:txtPassword    admin123




