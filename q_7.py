# program that prints the sum of the numbers in the string s

s = "1.23,2.4,3.123"
total = sum(map(float, s.split(",")))
print(total)