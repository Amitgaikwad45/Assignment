*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}  chrome
#&{url}      qa=https://www.ebay.com/    uat=http://uat.demo.com     dev=http://dev.demo.com
${url}      https://www.ebay.com/


*** Keywords ***
Start TestCase
    open browser    ${url}  ${browser}
    maximize browser window
    sleep    4s

Finish TestCase
    close browser
