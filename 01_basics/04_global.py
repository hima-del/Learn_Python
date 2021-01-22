x = "awesome"

def myfunction():
    x = "fantastic"
    print("python is "+x)

myfunction()
print("python is "+x)
#To create a global variable inside a function, you can use the global keyword
def myfun():
    global x
    x ="super"
myfun()
print("python is "+x)
    