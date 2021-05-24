*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Testing Frames
    open browser    https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html    chrome
    #switch to one frame to another
    select frame    packageListFrame    #give id name xpath
    click link    org.openqa.selenium
    unselect frame
    sleep    3

    select frame    packageFrame
    click link    WebDriver
    unselect frame
    sleep    3

    select frame    classFrame
    click link    Help
    unselect frame

    close browser