# number of local variables declared in a function
# Implementation of above approach

# A function containing 3 variables
def fun():
	a ,b= 1,20.95
	str = 'hello world'




print(fun.__code__.co_nlocals)
