#Post method used to create new resource on server
import requests
import json
import jsonpath
url="https://reqres.in/api/users"


#Read Input json file
file=open('C:/Users/afour/PycharmProjects/pythonProject/post.json','r')
json_input=file.read()
request_json=json.loads(json_input)
#print(request_json)

#make post with json request body
response=requests.post(url,request_json)
print(response.content)

assert response.status_code == 201

#fetch specific header
print(response.headers.get('Content-Length'))

#parse response to json format
res_json=json.loads(response.text)

#Pick ID using jsonpath it returns list of id's
ID=jsonpath.jsonpath(res_json,'id')

print(ID[0])

