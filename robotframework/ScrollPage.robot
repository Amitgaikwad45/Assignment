*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
ScrollingTest
    open browser    https://www.countries-ofthe-world.com/flags-of-the-world.html   chrome
    maximize browser window
    #scrollTo(horizontal,vertical)
   # execute javascript    window.scrollTo(0,1500)
    #specify the element which you are looking
    #scroll element into view    xpath://*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img

    #scroll till bottom of the page
    execute javascript    window.scrollTo(0,document.body.scrollHeight)

    sleep    3
    #go back to top of the page
    execute javascript    window.scrollTo(0,-document.body.scrollHeight)

    close window