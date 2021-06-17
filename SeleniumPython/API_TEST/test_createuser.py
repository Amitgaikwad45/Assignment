
import requests
import json
import jsonpath
url="https://reqres.in/api/users"

def test_create():
    #Read Input json file
    file=open('C:/Users/afour/PycharmProjects/pythonProject/post.json','r')
    json_input=file.read()
    request_json=json.loads(json_input)
    #print(request_json)
    response=requests.post(url,request_json)
    print(response.content)
    assert response.status_code == 201


def test_create_copy():
    #Read Input json file
    file=open('C:/Users/afour/PycharmProjects/pythonProject/post.json','r')
    json_input=file.read()
    request_json=json.loads(json_input)
    #print(request_json)
    response=requests.post(url,request_json)
    res_json=json.loads(response.text)
    ID=jsonpath.jsonpath(res_json,'id')
    print(ID[0])

