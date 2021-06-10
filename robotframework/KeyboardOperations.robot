#keyboard operations
*** Settings ***
Library    SeleniumLibrary




*** Variables ***
${url}      http://www.thetestingworld.com
${browser}      chrome



*** Test Cases ***
Login_Test
    open browser    ${url}  ${browser}
    maximize browser window
    click link    xpath://a[text()='Login']
    press key    name:username  hello
    press key    xpath://button[@type='submit']     \\13    #ascii value for enter key
    #open context menu    xpath:/html/body/div[2]/div[2]/div/div/div[2]/ul/li[4]/a/span
    #double click element    xpath://a[text()='Login']
    
    close window
