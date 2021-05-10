#check the number is in given range
def check_range(n):
    if n in range(10,20):
        print( "Number %s is in the range"%str(n))
    else :
        print("The number is not in given range.")
check_range(15)