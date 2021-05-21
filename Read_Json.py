import json

#open file
myjsonfile= open('C:/Users/Amit/PycharmProjects/pythonProject/JSONFile/emp.json','r')

#read data
jsondata=myjsonfile.read()

#parse the data and store to obj
obj=json.loads(jsondata)

print(str(obj['firstname']))

print(str(obj['lastname']))

print(str(obj['address']))

list=obj['address']
print(list)

print(list[0])
print(list[1])
print(len(list))

#reading data from json array
for i in range(len(list)):
    print("address of ",i,"is........")
    print("street",list[i].get("street"))
    print("city",list[i].get("city"))
    print("state", list[i].get("state"),end=" ")
    print()