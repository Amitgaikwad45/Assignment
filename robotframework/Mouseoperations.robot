*** Settings ***
Library    SeleniumLibrary




*** Test Cases ***
MouseActions
    open browser    http://swisnl.github.io/jQuery-contextMenu/demo.html    chrome
    maximize browser window
    #right click action and open the context menu
    open context menu    xpath://span[@class='context-menu-one btn btn-neutral']
    sleep    3

    #Double click action
    go to   http://testautomationpractice.blogspot.com/
    maximize browser window
    double click element    xpath://button[contains(text(),'Copy Text')]
    sleep    3

    #Drag and drop actions specify source and target element attribute
    go to   http://www.dhtml.goodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
    drag and drop    id:box6    id:box106
    sleep    5


    close window