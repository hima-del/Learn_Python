#a decorator is a function that takes another function
# as an argument and has some kind of functionality and returns another function

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function   

@decorator_function
def display():
    print("display function ran")

@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name,age))

display_info("john",34)    
display()
#decorated_display=decorator_function(display)
#decorated_display()         