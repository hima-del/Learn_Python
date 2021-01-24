def myfunction():
    print("hello")
myfunction()    
def funcn(*kids):
    print("the youngest child is "+kids[1])
funcn("anna","jenna","fenna")  
def function(child1,child2,child3):
    print("the youngest child is "+child3)
function(child3="ani",child2="rani",child1="jani")    
def my_func(**kid):
    print("his last name is "+kid["lname"])
my_func(fname="john",lname="doe")    