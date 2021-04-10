thisdict = {
    "name" : "John",
    "age" : 34,
    "place" : "new york"
}

x = thisdict["name"]
print(x) 

y= thisdict.get("place")
print(y)

z = thisdict.keys()
print(z)

a = thisdict.values()
print(a)

b = thisdict.items()
print(b)

if "name" in thisdict:
    print("yes")

thisdict["name"] = "jenna" 
print(thisdict.values())   

thisdict.update({"age" : 40})
print(thisdict.values())

#thisdict.pop("place")
#print(thisdict.items())

#thisdict.popitem()
#print(thisdict.items())

#for x in thisdict:
 #   print(x)

#for x in thisdict:
 #   print(thisdict[x])    

#for x in thisdict.keys():
 #   print(x) 

#for x in thisdict.values():
 #   print(x)   

#for x,y in thisdict.items():
 #   print(x,y)     
print(thisdict.items())
thisdict.update({"name" : "ann"})
print(thisdict)
thisdict.update({"job" : "web dveloper"})
print(thisdict)