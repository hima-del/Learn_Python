mydic={
    "name":"john",
    "age":25,
    "location":"USA"
}
#loop through a dictionary
#for x in mydic:
#    print(x)
 #   print(mydic[x])
for x in mydic.values():
     print(x)
for x in mydic.keys():
    print(x)    
#loop through both keys and values
for x,y in mydic.items():
    print(x,y)     
thisdic=mydic.copy()
print(thisdic)    
newdic=dict(thisdic)
print(newdic)
#nested dictionaries
myfamily={
    "child1":{
        "name":"anna",
        "age":30
    },
    "child2":{
        "name":"jenna",
        "age":35
    },
    "child3":{
        "name":"fenna",
        "age":40
    }
}
print(myfamily)