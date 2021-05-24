*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
HandlingAlerts
    open browser    http://testautomationpractice.blogspot.com/     chrome
    click element   xpath://div/button[text()='Click Me']     #opens alert
    sleep    3
    #closes the alert with accept of ok button
    handle alert    accept

    #closes the alert by click cancel button
    #handle alert    dismiss
    #handle alert    leave      #keep alert open
    #alert should be present    Press a button!      #verifies particular alert present or not closes alert window automatically
    #alert should not be present    Press a button!   #fails

    close browser