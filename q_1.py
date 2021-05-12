# Create a function to search an element x in the user i/p list and return its location(index) if found otherwise return -1
def search_ele(list1):
    ele=int(input("Enter element to be searched"))
    for i in range(len(list1)):

        if list1[i] == ele:
            return i

    return -1


lst = []

# number of elemetns as input
n = int(input())
print("Enter data")
# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst.append(ele)

print(search_ele(lst))


