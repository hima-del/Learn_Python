#default parameter value
#If we call the function without argument, it uses the default value:
def myfunction(country="USA"):
    print("I am from "+country)
myfunction("India")
myfunction("Canada")
myfunction()  
#passing list to function
def my_func(food):
    for x in food:
        print(x)
fruits=["apple","banana","orange"]
my_func(fruits)          
#return values
def myfunc(x):
    return 5*x
print(myfunc(10))    