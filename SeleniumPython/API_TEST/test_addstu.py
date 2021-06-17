import requests
import json
import jsonpath

def test_add_new_data():
    App_url="http://thetestingworldapi.com/api/studentsDetails"
    file = open('C:/Users/afour/PycharmProjects/pythonProject/post.json', 'r')
    request_json=json.loads(file.read())
    response=requests.post(App_url,request_json)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_api_url="http://thetestingworldapi.com/api/technicalskills"
    file = open('C:/Users/afour/PycharmProjects/pythonProject/techskill.json', 'r')
    request_json = json.loads(file.read())
    request_json['id']=int(id[0])
    request_json['st_id']=id[0]
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    add_url = "http://thetestingworldapi.com/api/addresses"
    file = open('C:/Users/afour/PycharmProjects/pythonProject/addresses.json', 'r')
    request_json = json.loads(file.read())
    request_json['stId']=id[0]
    response = requests.post(add_url, request_json)
    print(response.text)

    final_details="http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response=requests.get(final_details)
    print(response.text)