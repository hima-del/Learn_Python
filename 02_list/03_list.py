#copy list
thelist=["apple","orange","banana"]
mylist=thelist.copy()
print(mylist)
#another way to make copy
newlist=list(thelist)
print(newlist)
#join list
list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2
print(list3)
#another joining method is append()
for x in list2:
    list1.append(x)
print(list1)  
#another joining method is extend()  
list1.append(list2)
print(list1)