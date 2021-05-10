#remove the duplicate elements from the list
def Remove(duplicate):
    unique = []
    for num in duplicate:
        if num not in unique:
            unique.append(num)
    return unique


# Driver Code
duplicate = [1,2,3,3,3,3,4,5]
print(Remove(duplicate))
