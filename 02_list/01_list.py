thelist=["apple","orange","banana"]
veg=["carrot","tomato","potato"]
print(thelist)
print(thelist[1])
print(thelist[-1])
thelist[1]="pappaya"
print(thelist)
thelist.insert(3,"mango")
print(thelist)
thelist.insert(0,"cherry")
print(thelist)
thelist.append("blue berrry")
print(thelist)
thelist.extend(veg)
print(thelist)
print(veg)
#remove() removes specified item
thelist.remove("carrot")
print(thelist)
#pop() removes specified index
thelist.pop(0)
print(thelist)
del thelist[0]
print(thelist)
veg.clear()
print(veg)
print(thelist)
#loop through list
for i in range(len(thelist)):
    print(thelist[i])