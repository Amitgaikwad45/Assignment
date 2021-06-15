*** Settings ***
Library    XML
Library    OS
Library    Collections


*** Test Cases ***
TestCase1
    ${xml_obj}  parse xml    C:/Users/afour/PycharmProjects/robotframework/employee.xml

    #Validations

    #check single elment value

    ${emp_fnm}  get element text    ${xml_obj}  .//employee[1]/firstname
    should be equal    ${emp_fnm}   John

    #approach 2 by fetching element
    ${emp_fnm}  get element    ${xml_obj}   .//employee[1]/firstname
    should be equal    ${emp_fnm.text}  John

    #approach 3
    element text should be    ${xml_obj}    John    .//employee[1]/firstname

    #check multiple elements value
    ${cnt}  get element count    ${xml_obj}     .//employee
    should be equal as integers    ${cnt}   5


    #check attribute present
    element attribute should be    ${xml_obj}   id  be133   .//employee[5]

    #check values of child element
    ${child_ele}    get child elements    ${xml_obj}    .//employee[1]
    should not be empty    ${child_ele}

    ${fnm}  get element text    ${child_ele[0]}
    ${lnm}  get element text    ${child_ele[1]}
    ${title}  get element text    ${child_ele[2]}

    log to console    ${fnm}
    log to console    ${lnm}
    log to console    ${title}

    should be equal    ${fnm}       John
    should be equal    ${lnm}       Doe
    should be equal    ${title}     Engineer