# program to print largest odd among x,y,z

# Enter x
x=int(input("Enter x"))
# Enter y
y=int(input("Enter y"))\
# Enter z
z=int(input("Enter z"))

if x%2!=0 and y%2!=0 and z%2!=0 and x>y and x>z:
    print(x)
elif x%2!=0 and y%2!=0 and z%2!=0 and y>x and y>z:
    print(y)
elif x%2!=0 and y%2!=0 and z%2!=0 and z>x and z>y:
    print(z)
elif x%2==0 and y%2!=0 and z%2!=0 and y>z:
    print(y)
elif x%2==0 and y%2!=0 and z%2!=0 and z>y:
    print(z)
elif x%2!=0 and y%2!=0 and z%2==0 and y>x:
    print(y)
elif x%2!=0 and y%2!=0 and z%2==0 and x>y:
    print(x)
elif x%2!=0 and y%2==0 and z%2!=0 and x>z:
    print(x)
elif x%2!=0 and y%2==0 and z%2!=0 and z>x:
    print(z)
else:
    print('none of them are odd')