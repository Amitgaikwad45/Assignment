#rotation of list elements
# Python program to right rotate a list by n

# Returns the rotated list
def rightRotate(lists, num):
    output_list = []

    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    return output_list


# Driver Code


lst_1 = []

# number of elemetns as input
n = int(input("enter no of elements"))
print("Enter data")
# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst_1.append(ele)

rotate_num=int(input("Enter number for rotate"))
print(rightRotate(lst_1, rotate_num))
