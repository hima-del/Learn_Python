x=lambda a:a+10
print(x(5))
def myfunctn(n):
    return lambda a:a*n
mydoubler=myfunctn(2)
print(mydoubler(11))    