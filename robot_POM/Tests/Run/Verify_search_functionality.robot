*** Settings ***
Documentation  Basic Search Functionality
Resource  ../../Resources/Commonfunctionality.robot
Resource  ../../Resources/Pageobjects/HeaderPage.robot
Resource  ../../Resources/Pageobjects/SearchResultsPage.robot

Test Setup  Commonfunctionality.Start TestCase
Test Teardown  Commonfunctionality.Finish TestCase


*** Variables ***




*** Test Cases ***

Verify basic search functionality
    [Documentation]  This testcase verifies the basic search
    [Tags]  Functional

    HeaderPage.Input Search Text and Click Search
    SearchResultsPage.Verify Search Results

Verify advanced search functionality
    [Documentation]  This testcase verifies the advanced search
    [Tags]  Functional

    HeaderPage.Click on Advanced Search Link
