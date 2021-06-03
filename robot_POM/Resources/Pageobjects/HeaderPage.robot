*** Settings ***
Library  SeleniumLibrary


*** Variables ***
#scalar varible
#${search_txt}   books

#dictonary
&{search_txt}   abc=books   bcd=travel

*** Keywords ***
Input Search Text and Click Search
    input text    xpath://*[@id="gh-ac"]        ${search_txt.abc}
    press keys    xpath://*[@id="gh-btn"]   RETURN



Click on Advanced Search Link
    click element    xpath://*[@id="gh-as-a"]
