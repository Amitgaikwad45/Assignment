#testkeyword
*** Settings ***
Library     SeleniumLibrary
#specify file which contains locators
Variables    ../PageObjects/robotlocators.py



*** Keywords ***
Open my browser
    [Arguments]    ${url}    ${browser}
    open browser    ${url}  ${browser}
    maximize browser window
    sleep    3 seconds

click signin button
    click button            ${btn_signin}
    sleep    3 seconds

Switch tab
    ${window_handles}=      get window handles
    switch window    ${window_handles}[1]
    maximize browser window



Enter email
    [Arguments]    ${email}
    #locator refering from locators file
    input text    ${txt_email}      ${email}
    click button    ${btn_nxt}
    sleep    3 seconds




Enter password
    [Arguments]    ${password}
    #locator refering from locators file
    input text    ${txt_pwd}   ${password}
    click button    ${btn_nxt_pwd}
    sleep    3 seconds
    click button    ${btn_allow}
    sleep    2 seconds
    click element    ${link_txt}

Get username
    sleep    3 seconds
    ${window_handle2}=   get window handles
    switch window       ${window_handle2}[0]
    click button    ${nav_ele}
    ${usernm}=  get text    xpath://div[@class='profile-section']/div[1]/h2[@class='user-name']
    log to console    ${usernm}


Fetch all options
    ${Dashboard}=   get text    ${dboard}
    log to console    ${Dashboard}

    ${Skills}=     get text    ${skill}
    log to console    ${Skills}

    ${Timesheet}=   get text    ${tsheet}
    log to console    ${Timesheet}

    ${Reports}=     get text    ${reprt}
    log to console    ${Reports}

    ${PRS}=     get text    ${prs}
    log to console    ${PRS}

    ${tassesment}=      get text    ${ta}
    log to console    ${tassesment}

    ${lhcm}=        get text    ${lcm}
    log to console    ${lhcm}

    ${tms}=     get text    ${Tms}
    log to console    ${tms}

    ${lgout}=   get text    ${out_lg}
    log to console    ${lgout}


Enter Tms section
    click element    ${Tms}
    ${sw_window}=   get window handles
    switch window    ${sw_window}[1]
    sleep    5 seconds
    #click element    ${history}





Enter Raiseticket

    sleep    3 seconds
    click element    ${select_arrow}
    select from list by label   xpath://*[@id="mat-option-0" ]/span     Request
   # sleep    3 seconds
    #select from list by index

Enter title
    [Arguments]    ${title}

    #locator refering from locators file issue title
    input text    ${txt_title}      ${title}


Enter description
    #issue description
    [Arguments]    ${des}
    input text    ${txt_des}        ${des}


Enter History
    click element      ${sec_history}
    log to console      ${sec_his}



Enter logout btn
    sleep    3 seconds
    ${window_handle1}=   get window handles
    switch window       ${window_handle1}[0]
    click button    ${nav_ele}
    click element    ${btn_logout}
