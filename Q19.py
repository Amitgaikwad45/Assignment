#Write a Python program to access a function inside a function
def fun():
    print ("Hello from outer function")
    def f2():
        print ("Hello from inner function")
    f2()

fun()