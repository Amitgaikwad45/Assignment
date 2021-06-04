import json
import jsonpath


def read_locator_from_json(locatorname):
    f=open('C:/Users/Amit/PycharmProjects/robotframework/JsonFiles/Elements.json','r')
    response=json.loads(f.read())
    value=jsonpath.jsonpath(response,locatorname)
    return value[0]
