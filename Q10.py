#even numbers from a list

list1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
F=[]
for i in range(len(list1)):
    if(list1[i]%2==0):
        F.append(list1[i])


print(F)        