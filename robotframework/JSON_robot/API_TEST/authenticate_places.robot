#AIzaSyA2KlKyiywZ1nleZTWpiq9M-xhTTZ-biNo api key
#https://maps.googleapis.com/maps/api/place/nearbysearch/json?
#location=-33.8670522,151.1957362&radius=500&types=food&name=harbour&key=YOUR_API_KEY
*** Settings ***
Library    RequestsLibrary
Library    Collections


*** Variables ***
${url}      https://maps.googleapis.com
${req_url}      /maps/api/place/nearbysearch/json?


*** Test Cases ***
MapPlacesAPI
    Create Session    mysession     ${url}
    ${params}   create dictionary   location=33.8670522,151.1957362     radius=500      types=food      name=harbour    key=AIzaSyA2KlKyiywZ1nleZTWpiq9M-xhTTZ-biNo
    ${response}     get request    mysession    ${req_url}     params=${params}
    log to console    ${response.status_code}
    log to console    ${response.content}
