#sum all the elements in the list
total = 0


# creating a list
list1 = [11,5,17,18,23,'lemon',"783",1.0]

for x in list1:
    if x.__class__.__name__ in["int","float"]:
        total += x
    continue


print(total)
