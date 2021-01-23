#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a=200
b=20
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")  
else:
    print("a is greater than b")
#and
x=200
y=33
z=500
if x>y and z>x:
    print("both conditions are true")    
if x>y or x>z:
    print("atleast one condition is true")      
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a=33
b=200
if b>a:
    pass        
