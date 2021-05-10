#check given number is perfect or not
n = int(input("Enter any number: "))
sum = 0
for i in range(1, n):
    if(n % i == 0):
        sum = sum + i
if (sum == n):
    print("perfect")
else:
    print("not")