#Put method used to update resource on server
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
response=requests.put(url,request_json)
print(response.content)

assert response.status_code == 200

#parse response to json format
res_json=json.loads(response.text)

updated_list=jsonpath.jsonpath(res_json,'updatedAt')
print(updated_list[0])

