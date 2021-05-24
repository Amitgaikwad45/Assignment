*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
LoginTc
    open browser    https://opensource-demo.orangehrmlive.com/  chrome
    maximize browser window
    input text    id:txtUsername    Admin
    input text    id:txtPassword    admin123

    #capture element screenshot specify the path
    #capture element screenshot    xpath://div[@id='divLogo']/img      C:/Users/Amit/Pictures/Screenshots/Logo.png
    #capture page screenshot    C:/Users/Amit/Pictures/Screenshots/page.png

    #store screenshot at project directory
    capture element screenshot  xpath://div[@id='divLogo']/img  page.png
    capture page screenshot    Logo.png
