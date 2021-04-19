from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce(lambda x,y : x+y,li)
print(sum)

lis = [ 1 , 3, 5, 6, 2, ] 
print("the maximun element in the list is : ",end="")
print(reduce(lambda a,b:a if a>b else b,lis))