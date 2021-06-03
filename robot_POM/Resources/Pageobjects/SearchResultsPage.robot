*** Settings ***
Library  SeleniumLibrary
Resource    ./HeaderPage.robot

*** Variables ***
${search_res}   =   result for

*** Keywords ***
Verify Search Results
    page should contain    ${search_res}    ${search_txt.abc}
