#The map() function executes a specified function for each item in an iterable. 
# The item is sent to the function as a parameter.
def myfunc(n):
    return len(n)
x=map(myfunc,("apple","orange","banana"))
print(x)    
print(list(x))

def myfunction(a,b):
    return a+b
x=map(myfunction,("red","white","yellow"),("apple","milk","banana"))
print(list(x))    