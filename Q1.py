# Python program to find the maximum number among the three numbers

def maximum(a, b, c):
    if (a >= b) and (a >= c):
        max = a

    elif (b >= a) and (b >= c):
        max = b
    else:
        max = c

    return max


# Driven code
a = 10
b = 14
c = 12
print(maximum(a, b, c))
