*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
GetLinkCount
    open browser    https://www.nopcommerce.com/en/demo     chrome
    maximize browser window
    #count no of links present on particular page
    ${cnt}=     get element count    xpath://a
    log to console    ${cnt}

    @{linkitems}    create list

    #iterate over the count to get link text
     FOR    ${i}    IN RANGE    1       ${cnt}+1
        ${linktext}=    get text    xpath:(//a)[${i}]
        log to console    ${linktext}

     END
     close window
