thisdict={
    "name":"john",
    "age":25,
    "location":"USA"
}
x=thisdict["location"]
print(x)
y=thisdict.get("name")
print(y)
z=thisdict.keys()
#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
print(z) # before change
#Add a new item to the original dictionary, and see that the value list gets updated as well
thisdict["job"]="developer"
print(z)#after change
p=thisdict.values()
print(p)
#The items() method will return each item in a dictionary, as tuples in a list.
q=thisdict.items()
print(q)
#Check if Key Exists
if "age" in thisdict:
    print("age is one of the keys in this dictionary")
#update dictionary
thisdict.update({"age":30})
print(thisdict)    
#removing items
#The pop() method removes the item with the specified key name:
thisdict.pop("job")
print(thisdict)
thisdict.popitem()
print(thisdict)
#delete
del thisdict["age"]
print(thisdict) 
#del thisdict
#print(thisdict)
thisdict.clear()
print(thisdict)
