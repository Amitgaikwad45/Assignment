import requests
import json
import jsonpath
#API URL
url="https://reqres.in/api/users?page=2"

#send a GET request
response=requests.get(url)

#Display response content
#print(response.content)
#print(response.headers)

#parse response to json format
json_response=json.loads(response.text)
print(json_response)

#Fetch value using JSON path
pages=jsonpath.jsonpath(json_response,'total_pages') # jsonpath returns a list
print(pages[0])
assert  pages[0] == 2
