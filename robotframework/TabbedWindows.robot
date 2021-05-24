*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
TabbedWindowsTest
    open browser    http://demo.automationtesting.in/Windows.html   chrome
    maximize browser window
    sleep    3
    click element    xpath://*[@id='Tabbed']/a/button
    ${window_handles}=      get window handles
    ${window_identifiers}=  get window identifiers
    ${window_names}=    get window names
    ${window_title}=    get window titles


    switch window    ${window_handles}[1]
    click element    xpath://*[@id="navbar"]/a[2]
    close window
    sleep    3

    switch window    ${window_handles}[0]
    close window