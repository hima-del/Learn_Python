fruits=["apple","mango","cherry","banana"]
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)        
#list comprehension
new=[x for x in fruits if "n" in x]
print(new)
newvalue=[x for x in range(10)]
print(newvalue)
newval=[x.upper() for x in fruits]
print(newval)
val=["hello" for x in newvalue]
print(val)
#sort
newval.sort()
print(newval)
numbers=[100,10,11,50,5,55,82,8,23]
numbers.sort()
print(numbers)
#sort-descending
numbers.sort(reverse=True)
print(numbers)
#customise sort function
def myfunction(n):
    return abs(n-50)
thelist=[100,50,65,82,23]
thelist.sort(key=myfunction)
print(thelist)    
mylist=["banana","Orange","Kiwi","apple"]
mylist.sort()
print(mylist)
mylist.sort(key=str.upper)
print(mylist)
    