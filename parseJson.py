import requests
import json
import jsonpath

api_url="https://reqres.in/api/users?page=2"

#make a request
response1=requests.get(api_url)
print(response1.text)

#Validate status code
assert response1.status_code==200

#parse response into json format
json_res=json.loads(response1.text)
print(json_res)

#apply json path
x=jsonpath.jsonpath(json_res,'total')
print(x)

y=jsonpath.jsonpath(json_res,'data[1].first_name')
print(y)

for val in json_res['data']:
    print(val['first_name'])
