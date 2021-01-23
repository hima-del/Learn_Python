#A set is a collection which is both unordered and unindexed.
thisset={"apple","orange","banana"}
print(thisset)
#Once a set is created, you cannot change its items, but you can add new items.
#Sets cannot have two items with the same value.
newset={"a","b","b","c"}
print(newset)
theset=set(("king","queen","prince"))
print(theset)
for x in theset:
    print(x)
print("apple" in thisset)    
if "apple" in thisset:
    print("yes")
#add items
thisset.add("mango")
print(thisset)    
thisset.update(theset)
print(thisset)
#add any iterable
mylist={"kiwi","peer","anar","cherry","pine apple"}
thisset.update(mylist)
print(thisset)
print(type(thisset))
#remove 
mylist.remove("kiwi")
mylist.discard("peer")
print(mylist)
x=mylist.pop()
print("removed element",x)
print(mylist)