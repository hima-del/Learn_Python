#The try-except block can handle exceptions. 
# This prevents abrupt exits of the program on error
try:
    1/0
except ZeroDivisionError:
    print("divided by zero")
print("should reach here")

try:
    open("fantasy.txt")
except:
    print("something went wrong")
print("should reach here")       

try:
    x=input("enter number: ")
    x=x+1
    print(x)
except:
    print("invalid input")    