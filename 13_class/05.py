#first class functions

def square(x):
    return x*x

#f=square
#print(square)
#print(f)
#print(f(6))

def my_map(func,arg_list):
    result=[]
    for i in arg_list:
        result.append(func(i))
    return result
squares=my_map(square,[1,2,3,4,5])
print(squares)        

#function returning another function

def logger(msg):

    def log_message():
        print("log: ",msg)
    return log_message

log_hi=logger("hi")
print(log_hi)
print(log_hi())    

