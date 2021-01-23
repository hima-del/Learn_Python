#loop through tuple
thistuple=("apple","orange","banana")
print(thistuple)
for x in thistuple:
    print(x)
mytuple=tuple(("a","b","c","d"))
for x in range(len(mytuple)):
    print(mytuple[x])    
#join tuples
tuple3=thistuple+mytuple
print(tuple3)
#multiply tuples
newtuple=tuple3*3
print(newtuple)